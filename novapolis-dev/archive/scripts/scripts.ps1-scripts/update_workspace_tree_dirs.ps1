Param(
    [string]$Output = "workspace_tree_dirs.txt"
)

$timestamp = Get-Date -Format 'yyyy-MM-dd HH:mm'
$exclude = @('Backups', 'outputs', '.git', '.gitmodules', '.mypy_cache', '.pytest_cache', '__pycache__', '.venv', '.vscode', '.idea', '.vs', 'node_modules')
$root = (Get-Location).ProviderPath
$topDirs = Get-ChildItem -LiteralPath $root -Directory | Where-Object { $exclude -notcontains $_.Name } | Sort-Object Name

$lines = @("Filtered directories (excl. outputs, Backups, venv, caches)  $timestamp", "Top-Level")
foreach ($dir in $topDirs) {
    $lines += "  - $($dir.Name)"
}
$lines += ""

foreach ($dir in $topDirs) {
    $lines += "$($dir.Name)/"
    $subDirs = Get-ChildItem -LiteralPath $dir.FullName -Directory | Where-Object { $exclude -notcontains $_.Name } | Sort-Object Name
    if ($subDirs.Count -eq 0) {
        $lines += "  - (leer)"
    } else {
        foreach ($sub in $subDirs) {
            $lines += "  - $($sub.Name)"
        }
    }
    $lines += ""
}

$ascii = [System.Text.Encoding]::GetEncoding("us-ascii")
[System.IO.File]::WriteAllLines((Join-Path $root $Output), $lines, $ascii)
