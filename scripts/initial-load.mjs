import { readFile, stat } from "node:fs/promises";
import path from "node:path";

const ROOT = path.resolve(import.meta.dirname, "..");
const html = await readFile(path.join(ROOT, "index.html"), "utf8");

// Divide por slides usando data-slide="N"
const parts = html.split(/data-slide="(\d+)"/);
// parts: [before, "1", contentAfter1Marker, "2", ...] aprox; reconstruimos rangos por aparicion
const slideMedia = {};
const re = /data-slide="(\d+)"[\s\S]*?(?=data-slide="\d+"|$)/g;
let m;
while ((m = re.exec(html))) {
  const n = m[1];
  const block = m[0];
  const files = new Set();
  for (const rx of [/data-src="(\.\/[^"]+)"/g, /data-vsrc="(\.\/[^"]+)"/g, /data-bg="(\.\/[^"]+)"/g]) {
    let mm;
    while ((mm = rx.exec(block))) files.add(mm[1]);
  }
  slideMedia[n] = files;
}

async function sizeOf(set) {
  let total = 0;
  for (const ref of set) {
    try {
      total += (await stat(path.join(ROOT, ref.replace(/^\.\//, "")))).size;
    } catch {}
  }
  return total;
}

// Carga inicial real: slide 1 (CSS bg) + slide 1 media + slide 2 + slide 3 (preload vecino)
const heroBg = (await stat(path.join(ROOT, "control biologico.webp"))).size;
const s1 = await sizeOf(slideMedia["1"] || new Set());
const s2 = await sizeOf(slideMedia["2"] || new Set());
const s3 = await sizeOf(slideMedia["3"] || new Set());

console.log("Media por slide (KB):");
for (const n of Object.keys(slideMedia).sort((a, b) => a - b)) {
  console.log(`  slide ${n}: ${((await sizeOf(slideMedia[n])) / 1024).toFixed(0)} KB  (${slideMedia[n].size} archivos)`);
}
console.log(`\nFondo portada (CSS): ${(heroBg / 1024).toFixed(0)} KB`);
console.log(`\n=== CARGA INICIAL (portada + slide 2 + preload slide 3) ===`);
console.log(`${((heroBg + s1 + s2 + s3) / 1024 / 1024).toFixed(2)} MB`);
