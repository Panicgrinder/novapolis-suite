/*
  Speicher-optimierter Chat-Exporter
  - Startet Auto-Scroll nach 10s
  - Hört auf, wenn 20s keine neuen Nachrichten auftauchen
  - Minimaler RAM‑Footprint:
    • Wenn verfügbar, wird direkt in eine Datei gestreamt (File System Access API)
    • Fallback: Chunked-Downloads (mehrere Teile), um RAM niedrig zu halten
  - Nutzt MutationObserver für neue DOM‑Nachrichten statt ständiger Vollscans
*/

/*
  Speicher-optimierter Chat-Exporter (verbesserte Version)
  Für Chrome / Edge / Brave
  --------------------------------------------
  - Erkennt automatisch den Scroll-Container
  - Auto-Scroll startet nach 10 Sekunden
  - Stoppt, wenn 20s keine neuen Nachrichten
  - Minimaler RAM-Verbrauch:
    • Stream direkt in Datei (File System Access API)
    • Fallback: Chunked-Downloads (mehrere Teile)
  - Nutzt MutationObserver für neue Nachrichten
  --------------------------------------------
*/

(async () => {
  console.log("⚙️ Chat-Export gestartet – bitte nicht scrollen oder tippen.");

  const SETTINGS = {
    BATCH_SIZE: 200,                // Trenner alle 200 Nachrichten
    MAX_SAFE: 5000,                 // Abbruch bei zu vielen Nachrichten
    START_SCROLL_AFTER_MS: 10000,   // Auto-Scroll-Start nach 10s
    SCAN_INTERVAL_MS: 500,          // Fallback-Scan alle 0.5s
  SCROLL_INTERVAL_MS: 1000,       // Scroll alle 1.0s (etwas schneller, lädt Nachschub zügiger)
    NO_NEW_TIMEOUT_MS: 20000,       // Abbruch, wenn 20s keine neuen Nachrichten
    MAX_DURATION_MS: 10 * 60 * 1000,// Sicherheitslimit 10 Minuten
    CHUNK_FLUSH_THRESHOLD: 1_000_000 // ~1 MB pro Chunk
  };

  const supportsFS = typeof window.showSaveFilePicker === 'function';
  const isoName = `RAW-chat-export-${new Date().toISOString().replace(/[:.]/g, '-')}.txt`;

  let fileHandle = null;
  let writer = null;
  let chunkBuffer = '';
  let chunkIndex = 1;

  async function ensureOutputReady() {
    if (writer || chunkBuffer !== '') return;
    if (supportsFS) {
      try {
        console.warn('ℹ️ Speicherort: database-raw/99-exports/');
        fileHandle = await window.showSaveFilePicker({
          suggestedName: isoName,
          types: [{ description: 'Text', accept: { 'text/plain': ['.txt'] } }]
        });
        writer = await fileHandle.createWritable();
        await writer.write(`# Chat-Export\n\n`);
      } catch (e) {
        console.warn('⚠️ Dateiauswahl abgelehnt oder nicht verfügbar – wechsle zu Chunk-Modus.', e);
      }
    }
  }

  async function writeOut(text) {
    if (writer) {
      await writer.write(text);
    } else {
      chunkBuffer += text;
      if (chunkBuffer.length >= SETTINGS.CHUNK_FLUSH_THRESHOLD) await flushChunk();
    }
  }

  async function flushChunk(force = false) {
    if (!writer && (force || chunkBuffer.length >= SETTINGS.CHUNK_FLUSH_THRESHOLD)) {
      const name = isoName.replace(/\.txt$/, `-part-${String(chunkIndex).padStart(3, '0')}.txt`);
      const blob = new Blob([chunkBuffer], { type: 'text/plain;charset=utf-8' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = name;
      document.body.appendChild(a);
      a.click();
      await new Promise(r => setTimeout(r, 200)); // kurze Pause
      URL.revokeObjectURL(a.href);
      document.body.removeChild(a);
      console.log(`💾 Chunk ${chunkIndex} gespeichert (${chunkBuffer.length} Zeichen).`);
      chunkIndex++;
      chunkBuffer = '';
    }
  }

  async function finalizeOutput(totalCount) {
    if (writer) await writer.close();
    else if (chunkBuffer.length) await flushChunk(true);
    console.log(`✅ Export abgeschlossen: ${totalCount} Nachrichten.`);
  }

  // DOM-Helfer
  const getNodes = () => Array.from(document.querySelectorAll('[data-message-author-role]'));
  const markExported = (el) => { try { el.dataset.cvnExported = '1'; } catch(_){} };

  let totalMessages = 0;
  let lastNewAt = Date.now();
  const startAt = Date.now();
  let blockCounter = 0;

  async function processNode(el) {
    if (!el || el.dataset.cvnExported === '1') return false;
    const role = el.getAttribute('data-message-author-role') || 'unknown';
    const contentEl = el.querySelector('.markdown.prose, [data-testid="markdown"]');
    const text = (contentEl ? contentEl.innerText : el.innerText || '').trim();
    // Skippe leere Nachrichten: nicht zählen/schreiben/markieren,
    // damit spätere dynamische Inhalte noch erfasst werden können.
    if (!text) return false;
    totalMessages++;
    blockCounter++;
    const ts = new Date().toISOString();
    const header = `### ${totalMessages} [${role}] @ ${ts}\n`;
    const body = `${text}\n\n`;
    const sep = (blockCounter >= SETTINGS.BATCH_SIZE) ? `---\n\n` : '';
    if (sep) blockCounter = 0;
    await writeOut(header + body + sep);
    markExported(el);
    return true;
  }

  async function processExistingNodesOnce() {
    const nodes = getNodes();
    let added = 0;
    for (const n of nodes) {
      if (totalMessages >= SETTINGS.MAX_SAFE) break;
      const did = await processNode(n);
      if (did) added++;
    }
    if (added) {
      lastNewAt = Date.now();
      console.log(`🧩 Initial gesammelt: ${added} (gesamt: ${totalMessages}).`);
    }
  }

  await ensureOutputReady();
  await processExistingNodesOnce();

  // Auto-Scroll-Fix für verschachtelte Container
  function getScrollTarget() {
    const els = document.querySelectorAll('*');
    for (const el of els) {
      if (el.scrollHeight > el.clientHeight + 50 && getComputedStyle(el).overflowY !== 'visible') {
        return el;
      }
    }
    return window; // Fallback
  }
  const scrollTarget = getScrollTarget();
  console.log("🌀 Scroll-Ziel erkannt:", scrollTarget.tagName || 'window');

  if (SETTINGS.START_SCROLL_AFTER_MS > 0)
    await new Promise(r => setTimeout(r, SETTINGS.START_SCROLL_AFTER_MS));

  // MutationObserver für neue Nachrichten
  const observer = new MutationObserver(async (mutations) => {
    let added = 0;
    for (const m of mutations) {
      for (const node of m.addedNodes) {
        if (!(node instanceof Element)) continue;
        if (node.matches?.('[data-message-author-role]')) {
          if (await processNode(node)) added++;
        }
        const candidates = node.querySelectorAll?.('[data-message-author-role]');
        if (candidates?.length) {
          for (const el of candidates) {
            if (await processNode(el)) added++;
            if (totalMessages >= SETTINGS.MAX_SAFE) break;
          }
        }
        if (totalMessages >= SETTINGS.MAX_SAFE) break;
      }
      if (totalMessages >= SETTINGS.MAX_SAFE) break;
    }
    if (added) lastNewAt = Date.now();
  });
  observer.observe(document.body, { childList: true, subtree: true });

  // Auto-Scroll mit erkannten Container
  const scrollTimer = setInterval(() => {
    try {
      if (scrollTarget === window) {
        window.scrollTo(0, document.documentElement.scrollHeight);
      } else if (typeof scrollTarget.scrollTo === 'function') {
        scrollTarget.scrollTo(0, scrollTarget.scrollHeight);
      } else {
        // Fallback für Elemente ohne scrollTo
        scrollTarget.scrollTop = scrollTarget.scrollHeight;
      }
    } catch (e) {}
  }, SETTINGS.SCROLL_INTERVAL_MS);

  // Hauptloop
  while (true) {
  // Safety-first: Vollscan aller Nachrichten-Knoten, um nichts zu verpassen.
  // Deduplizierung passiert über el.dataset.cvnExported in processNode.
  const nodes = getNodes();
    for (const n of nodes) {
      if (n.dataset.cvnExported === '1') continue;
      const did = await processNode(n);
      if (did) lastNewAt = Date.now();
      if (totalMessages >= SETTINGS.MAX_SAFE) break;
    }

    if (totalMessages >= SETTINGS.MAX_SAFE) {
      console.warn("⚠️ Sicherheitslimit erreicht. Export beendet.");
      break;
    }
    if (Date.now() - lastNewAt >= SETTINGS.NO_NEW_TIMEOUT_MS) {
      console.log("⏹️ Keine neuen Daten – stoppe Export.");
      break;
    }
    if (Date.now() - startAt >= SETTINGS.MAX_DURATION_MS) {
      console.warn("⏱️ Maximaldauer erreicht. Export beendet.");
      break;
    }
    await new Promise(r => setTimeout(r, SETTINGS.SCAN_INTERVAL_MS));
  }

  clearInterval(scrollTimer);
  observer.disconnect();
  await finalizeOutput(totalMessages);
})();
