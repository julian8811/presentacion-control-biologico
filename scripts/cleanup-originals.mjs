import { readdir, access, unlink, stat } from "node:fs/promises";
import path from "node:path";

const ROOT = path.resolve(import.meta.dirname, "..");
const entries = await readdir(ROOT, { withFileTypes: true });
const exts = new Set([".jpeg", ".jpg", ".png"]);

let removed = 0;
let freed = 0;
for (const e of entries) {
  if (!e.isFile()) continue;
  const ext = path.extname(e.name).toLowerCase();
  if (!exts.has(ext)) continue;
  const webpTwin = path.join(ROOT, e.name.replace(/\.(jpeg|jpg|png)$/i, ".webp"));
  try {
    await access(webpTwin);
    const sz = (await stat(path.join(ROOT, e.name))).size;
    await unlink(path.join(ROOT, e.name));
    removed++;
    freed += sz;
  } catch {
    console.log("Conservado (sin webp):", e.name);
  }
}
console.log(`\nOriginales eliminados: ${removed}`);
console.log(`Espacio liberado: ${(freed / 1024 / 1024).toFixed(1)} MB`);
