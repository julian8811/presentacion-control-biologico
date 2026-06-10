import { mkdir, rename, unlink, readdir } from "node:fs/promises";
import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";

const ROOT = path.resolve(import.meta.dirname, "..");
const IMG = path.join(ROOT, "assets", "images");
const VID = path.join(ROOT, "assets", "videos");
const DOCS = path.join(ROOT, "docs");

await mkdir(IMG, { recursive: true });
await mkdir(VID, { recursive: true });
await mkdir(DOCS, { recursive: true });

const entries = await readdir(ROOT, { withFileTypes: true });
for (const e of entries) {
  if (!e.isFile()) continue;
  const ext = path.extname(e.name).toLowerCase();
  if (ext === ".webp") await rename(path.join(ROOT, e.name), path.join(IMG, e.name));
  else if (ext === ".mp4") await rename(path.join(ROOT, e.name), path.join(VID, e.name));
  else if ((ext === ".md" && e.name !== "README.md") || ext === ".docx")
    await rename(path.join(ROOT, e.name), path.join(DOCS, e.name));
}

const remove = [
  "Presentacion_Control_Biologico.html",
  "clean_presentation.py",
  "delete_slides.py",
  "update_presentation.py",
];
for (const f of remove) {
  try {
    await unlink(path.join(ROOT, f));
    console.log("Eliminado:", f);
  } catch {
    console.log("No encontrado:", f);
  }
}

let html = await readFile(path.join(ROOT, "index.html"), "utf8");

// Slide 18 dentro del contenedor de diapositivas
html = html.replace(
  /  <\/section>\r?\n\r?\n<\/div>\r?\n\r?\n\r?\n  <!-- ===== SLIDE 18: Evaluación ===== -->/,
  "  </section>\n\n  <!-- ===== SLIDE 18: Evaluación ===== -->",
);
html = html.replace(
  /    <span class="slide-number">18 \/ 18<\/span>\r?\n  <\/section>\r?\n\r?\n<\/div>/,
  '    <span class="slide-number">18 / 18</span>\n  </section>\n\n</div>',
);

// Rutas de medios
html = html.replace(/\.\/([^"']+\.webp)/g, "assets/images/$1");
html = html.replace(/\.\/([^"']+\.mp4)/g, "assets/videos/$1");
html = html.replace(/url\('assets\/images\//g, "url('assets/images/");

await writeFile(path.join(ROOT, "index.html"), html, "utf8");
console.log("index.html actualizado con rutas assets/");
