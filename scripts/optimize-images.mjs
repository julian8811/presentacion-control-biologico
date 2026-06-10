import sharp from "sharp";
import { readdir, readFile, writeFile, stat } from "node:fs/promises";
import path from "node:path";

const ROOT = path.resolve(import.meta.dirname, "..");
const IMG_DIR = path.join(ROOT, "assets", "images");
const HTML = path.join(ROOT, "index.html");
const MAX_DIM = 1600;
const QUALITY = 80;

const exts = new Set([".jpeg", ".jpg", ".png"]);

const entries = await readdir(IMG_DIR, { withFileTypes: true }).catch(() => []);
const images = entries
  .filter((e) => e.isFile() && exts.has(path.extname(e.name).toLowerCase()))
  .map((e) => e.name);

let html = await readFile(HTML, "utf8");
let totalBefore = 0;
let totalAfter = 0;
const renamed = [];

for (const name of images) {
  const src = path.join(IMG_DIR, name);
  const webpName = name.replace(/\.(jpeg|jpg|png)$/i, ".webp");
  const dest = path.join(IMG_DIR, webpName);

  const before = (await stat(src)).size;
  await sharp(src)
    .rotate()
    .resize({ width: MAX_DIM, height: MAX_DIM, fit: "inside", withoutEnlargement: true })
    .webp({ quality: QUALITY, effort: 5 })
    .toFile(dest);
  const after = (await stat(dest)).size;

  totalBefore += before;
  totalAfter += after;

  const refFrom = `assets/images/${name}`;
  const refTo = `assets/images/${webpName}`;
  if (html.includes(refFrom)) {
    html = html.split(refFrom).join(refTo);
    renamed.push(name);
  }
  console.log(
    `${name}  ${(before / 1024 / 1024).toFixed(2)}MB -> ${(after / 1024).toFixed(0)}KB  ${html.includes(webpName) ? "(ref updated)" : "(not referenced)"}`,
  );
}

await writeFile(HTML, html, "utf8");

console.log("\n=== RESUMEN IMAGENES ===");
console.log(`Imagenes convertidas: ${images.length}`);
console.log(`Referencias actualizadas en HTML: ${renamed.length}`);
console.log(`Total antes: ${(totalBefore / 1024 / 1024).toFixed(1)} MB`);
console.log(`Total despues: ${(totalAfter / 1024 / 1024).toFixed(1)} MB`);
console.log(`Reduccion: ${(100 - (totalAfter / totalBefore) * 100).toFixed(1)}%`);
