const umlautMap = {
  Ä: 'Ae', Ö: 'Oe', Ü: 'Ue', ä: 'ae', ö: 'oe', ü: 'ue', ß: 'ss'
};

function transliterateUmlauts(str) {
  return str.replace(/[ÄÖÜäöüß]/g, (m) => umlautMap[m] || m);
}

export function canonicalBasename(name) {
  // 1) Trim and transliterate umlauts
  let s = transliterateUmlauts(name.trim());
  // 2) Replace spaces and underscores with hyphens
  s = s.replace(/[ _]+/g, '-');
  // 3) Remove parentheses and other punctuation except hyphen and dot
  s = s.replace(/[()\[\]{}'"!?,;:+*\\/]+/g, '');
  // 4) Collapse multiple hyphens
  s = s.replace(/-+/g, '-');
  // 5) Remove leading/trailing hyphens
  s = s.replace(/^-+|-+$/g, '');
  return s;
}

export function canonicalFilename(filename) {
  const idx = filename.lastIndexOf('.');
  if (idx === -1) return canonicalBasename(filename);
  const base = filename.slice(0, idx);
  const ext = filename.slice(idx).toLowerCase();
  return canonicalBasename(base) + ext;
}
