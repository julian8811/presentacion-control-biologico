import { readFile, access, stat } from "node:fs/promises";
import path from "node:path";

const ROOT = path.resolve(import.meta.dirname, "..");
const html = await readFile(path.join(ROOT, "index.html"), "utf8");

const refs = new Set();
const patterns = [
  /data-src="(\.\/[^"]+)"/g,
  /data-vsrc="(\.\/[^"]+)"/g,
  /data-bg="(\.\/[^"]+)"/g,
  /url\('(\.\/[^']+\.(?:webp|png|jpe?g))'\)/g,
  /\bimg:\s*'(\.\/[^']+)'/g,
];
for (const re of patterns) {
  let m;
  while ((m = re.exec(html))) refs.add(m[1]);
}

let missing = 0;
let totalBytes = 0;
for (const ref of [...refs].sort()) {
  const file = path.join(ROOT, ref.replace(/^\.\//, ""));
  try {
    await access(file);
    totalBytes += (await stat(file)).size;
  } catch {
    missing++;
    console.log("FALTA:", ref);
  }
}

// Detectar restos sin optimizar
const leftover = [
  ["src=\"./*.jpeg (sin diferir)", /\ssrc="\.\/[^"]+\.jpe?g"/g],
  ["autoplay restante", /<video[^>]*\sautoplay/g],
  [".mp4 con src directo", /<video\s+src="/g],
];
console.log("\n=== CHEQUEOS ===");
for (const [label, re] of leftover) {
  const n = (html.match(re) || []).length;
  console.log(`${label}: ${n}`);
}

console.log("\n=== RESUMEN ===");
console.log(`Archivos referenciados: ${refs.size}`);
console.log(`Faltantes: ${missing}`);
console.log(`Peso total de medios referenciados: ${(totalBytes / 1024 / 1024).toFixed(1)} MB`);
console.log(`Tamano index.html: ${(Buffer.byteLength(html) / 1024).toFixed(0)} KB`);
