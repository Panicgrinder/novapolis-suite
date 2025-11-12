<#
.SYNOPSIS
    Append an entry to novapolis_agent/docs/DONELOG.txt and optionally commit & push.

.DESCRIPTION
    Safe wrapper to add a single-line DONELOG entry (timestamp | author | message).
    Designed to be executed via: pwsh -NoProfile -File scripts/append_done_and_push.ps1 -Message "..." -Push -Yes

.PARAMETER Message
    The message/body for the DONELOG entry. If omitted a sensible default is used.

.PARAMETER Author
    Optional author name. If omitted, tries git config user.name, falls back to $env:USERNAME.

.PARAMETER Push
    If specified, will perform `git push` after commit.

.PARAMETER Yes
    If specified, skip interactive confirmations.

EXAMPLE
    pwsh -NoProfile -File .\scripts\append_done_and_push.ps1 -Message "Fix: update docs" -Push -Yes
#>

param(
    [string]$Message,
    [string]$Author,
    [switch]$Push,
    [switch]$Yes,
    [switch]$AlsoRoot,
    [string[]]$Files,
    [string]$Checks
)

try {
    $ErrorActionPreference = 'Stop'

    # Determine repository root (one level up from script dir)
    $scriptDir = Split-Path -Parent $PSCommandPath
    $root = (Resolve-Path (Join-Path $scriptDir '..')).Path

    # DONELOG path
    $donePath = Join-Path $root 'novapolis_agent\docs\DONELOG.txt'

    # Determine author
    if (-not $Author) {
        try {
            $gitAuthor = (& git config user.name) -join ''
        } catch {
            $gitAuthor = $null
        }
        if (-not [string]::IsNullOrWhiteSpace($gitAuthor)) { $Author = $gitAuthor } else { $Author = $env:USERNAME }
    }

    # Default message uses latest commit short SHA if available
    if (-not $Message) {
        try {
            $sha = (& git rev-parse --short HEAD) -join ''
            if ($LASTEXITCODE -eq 0 -and $sha) { $Message = "Update related to commit $sha" } else { $Message = 'Update: documentation' }
        } catch {
            $Message = 'Update: documentation'
        }
    }

    # Determine target files to update their frontmatter
    if ($Files -and $Files.Count -gt 0) {
        $targetFiles = $Files
    } else {
        # Default: files from the last commit (HEAD)
        try {
            $changed = (& git show --name-only --pretty="" HEAD) -join "`n"
            $targetFiles = $changed -split "`n" | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne '' }
        } catch {
            $targetFiles = @()
        }
    }

    # Normalize paths and filter file types; skip the canonical exception file
    $skipPaths = @('.github/copilot-instructions.md')
    $filePatterns = @('*.md','*.markdown','*.txt','*.ps1','*.yml','*.yaml','*.json','*.mdx')
    $filesToProcess = @()
    foreach ($f in $targetFiles) {
        if (-not $f) { continue }
        $abs = Join-Path $root $f
        if ($skipPaths -contains ($f -replace '\\','/')) { Write-Host "Skipping SSOT exception: $f" -ForegroundColor Yellow; continue }
        if (-not (Test-Path $abs)) { continue }
        $ext = [System.IO.Path]::GetExtension($abs).ToLower()
        if ($filePatterns -contains "*${ext.TrimStart('.')}" -or $filePatterns -contains "*${ext}") {
            $filesToProcess += $abs
        } else {
            # also allow explicit match by extension
            if ($ext -in '.md','.markdown','.txt','.ps1','.yml','.yaml','.json','.mdx') { $filesToProcess += $abs }
        }
    }

    # Prepare timestamp and entry
    $ts = Get-Date -Format 'yyyy-MM-dd HH:mm'
    $entry = "$ts | $Author | $Message"

    Write-Host "Files detected for frontmatter update:`n$($filesToProcess -join "`n")`n" -ForegroundColor Cyan

    # Backup and update frontmatter for each file
    $backups = @()
    foreach ($file in $filesToProcess) {
        try {
            $bak = "$file.bak"
            Copy-Item -Path $file -Destination $bak -Force
            $backups += $bak

            $text = Get-Content -Raw -LiteralPath $file -Encoding UTF8

            # Detect existing YAML frontmatter (use (?s) singleline modifier for .NET regex)
            if ($text -match '(?s)^(---\s*\r?\n)(.*?)(\r?\n---\s*\r?\n)(.*)$') {
                $prefix = $Matches[1]
                $yaml = $Matches[2]
                $suffix = $Matches[4]

                # Simple parse: replace or add keys by regex
                # Update 'stand'
                if ($yaml -match "(^|\n)stand:\s*(.*)" ) {
                    $yaml = $yaml -replace "(^|\n)stand:\s*.*", "`nstand: $ts"
                } else {
                    $yaml = "stand: $ts`n$yaml"
                }

                # Update 'update'
                if ($yaml -match "(^|\n)update:\s*(.*)") {
                    $yaml = $yaml -replace "(^|\n)update:\s*.*", "`nupdate: $Message"
                } else {
                    $yaml = "update: $Message`n$yaml"
                }

                # Update 'checks' if provided
                if ($Checks) {
                    if ($yaml -match "(^|\n)checks:\s*(.*)") {
                        $yaml = $yaml -replace "(^|\n)checks:\s*.*", "`nchecks: $Checks"
                    } else {
                        $yaml = "checks: $Checks`n$yaml"
                    }
                }

                $newText = "---`n$yaml`n---`n$suffix"
            } else {
                # No frontmatter: create one
                $yaml = "stand: $ts`nupdate: $Message"
                if ($Checks) { $yaml = "$yaml`nchecks: $Checks" }
                $newText = "---`n$yaml`n---`n$text"
            }

            # Ensure single trailing newline
            $newText = $newText.TrimEnd("`r","`n") + "`n"

            # Write back as UTF8 (no BOM)
            Set-Content -LiteralPath $file -Value $newText -Encoding utf8
            Write-Host "Updated frontmatter: $file" -ForegroundColor Green

            } catch {
            Write-Error "Failed to update $($file): $($_)"
            # On error, restore backups
            foreach ($b in $backups) { try { Copy-Item -Path $b -Destination ($b -replace '\.bak$','') -Force } catch { Write-Verbose $_ } }
            exit 5
        }
    }

    # Run frontmatter validator if any files were processed
    if ($filesToProcess.Count -gt 0) {
        $validator = Join-Path $root 'scripts\run_frontmatter_validator.ps1'
        if (Test-Path $validator) {
            Write-Host 'Running frontmatter validator...' -ForegroundColor Cyan
            & pwsh -NoProfile -File $validator -Paths $filesToProcess
            if ($LASTEXITCODE -ne 0) {
                Write-Error "Frontmatter validator failed (exit $LASTEXITCODE). Restoring backups and aborting."
                foreach ($b in $backups) { Copy-Item -Path $b -Destination ($b -replace '\.bak$','') -Force }
                exit 6
            }
            Write-Host 'Frontmatter validator: PASS' -ForegroundColor Green
        } else {
            Write-Host "Validator not found: $validator - skipping validation" -ForegroundColor Yellow
        }
    }

    # Ensure DONELOG exists
    if (-not (Test-Path $donePath)) {
        New-Item -Path $donePath -ItemType File -Force | Out-Null
    }

    # Show planned change
    Write-Host "Planned DONELOG entry:`n$entry`nFile: $donePath" -ForegroundColor Cyan

    if (-not $Yes) {
        $ops = 'git add/commit'
        if ($Push) { $ops = $ops + '/push' }
        $confirm = Read-Host ("Append entry and ($ops)? Type 'yes' to continue")
        if ($confirm -ne 'yes') { Write-Host 'Aborted by user.'; exit 2 }
    }

    # Append to agent DONELOG
    Add-Content -LiteralPath $donePath -Value $entry -Encoding UTF8
    Write-Host "Appended DONELOG entry to: $donePath" -ForegroundColor Green

    # Optionally append to root DONELOG.md
    $toAdd = @($donePath)
    if ($AlsoRoot) {
        $rootDone = Join-Path $root 'DONELOG.md'
        if (-not (Test-Path $rootDone)) { New-Item -Path $rootDone -ItemType File -Force | Out-Null }
        Add-Content -LiteralPath $rootDone -Value $entry -Encoding UTF8
        Write-Host "Also appended to root DONELOG: $rootDone" -ForegroundColor Green
        $toAdd += $rootDone
    }

    # Git add & commit (include any frontmatter-updated files)
    $allToAdd = @()
    $allToAdd += $toAdd
    $allToAdd += $filesToProcess | Where-Object { Test-Path $_ }
    if ($allToAdd.Count -gt 0) {
        & git add -- $allToAdd
    }

    $commitMsg = "docs(donelog): $Message"

    # Use a temporary file for the message to avoid quoting issues
    $tmp = Join-Path $env:TEMP ("donelog_msg_{0}.txt" -f ([guid]::NewGuid().ToString()))
    Set-Content -Path $tmp -Value $commitMsg -Encoding UTF8
    try {
        & git commit -F $tmp | Out-Null
        if ($LASTEXITCODE -ne 0) { Write-Host "git commit failed or nothing to commit (exit $LASTEXITCODE)."; Remove-Item -LiteralPath $tmp -Force -ErrorAction SilentlyContinue; exit 3 }
    } finally {
        Remove-Item -LiteralPath $tmp -Force -ErrorAction SilentlyContinue
    }

    Write-Host "Committed DONELOG and frontmatter updates." -ForegroundColor Green

    if ($Push) {
        & git push
        if ($LASTEXITCODE -ne 0) { Write-Host 'git push failed.'; exit 4 }
        Write-Host 'Pushed to remote.' -ForegroundColor Green
    }

    Write-Host 'Complete.' -ForegroundColor Green
    exit 0

} catch {
    Write-Error "Error: $_"
    exit 1
}
