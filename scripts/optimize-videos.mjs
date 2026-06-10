import { execFile } from "node:child_process";
import { promisify } from "node:util";
import { readdir, stat, rename, unlink } from "node:fs/promises";
import path from "node:path";
import ffmpegPath from "ffmpeg-static";

const run = promisify(execFile);
const ROOT = path.resolve(import.meta.dirname, "..");

const entries = await readdir(ROOT, { withFileTypes: true });
const videos = entries
  .filter((e) => e.isFile() && path.extname(e.name).toLowerCase() === ".mp4")
  .map((e) => e.name);

let totalBefore = 0;
let totalAfter = 0;

for (const name of videos) {
  const src = path.join(ROOT, name);
  const tmp = path.join(ROOT, name.replace(/\.mp4$/i, ".opt.mp4"));
  const before = (await stat(src)).size;

  await run(ffmpegPath, [
    "-y",
    "-i", src,
    "-vf", "scale='min(1280,iw)':-2",
    "-c:v", "libx264",
    "-profile:v", "high",
    "-pix_fmt", "yuv420p",
    "-preset", "slow",
    "-crf", "30",
    "-an",
    "-movflags", "+faststart",
    tmp,
  ]);

  const after = (await stat(tmp)).size;
  // Solo reemplaza si quedo mas pequeno
  if (after < before) {
    await unlink(src);
    await rename(tmp, src);
    totalBefore += before;
    totalAfter += after;
    console.log(`${name}  ${(before / 1024 / 1024).toFixed(2)}MB -> ${(after / 1024 / 1024).toFixed(2)}MB`);
  } else {
    await unlink(tmp);
    totalBefore += before;
    totalAfter += before;
    console.log(`${name}  ${(before / 1024 / 1024).toFixed(2)}MB (sin cambios, original mas pequeno)`);
  }
}

console.log("\n=== RESUMEN VIDEOS ===");
console.log(`Videos procesados: ${videos.length}`);
console.log(`Total antes: ${(totalBefore / 1024 / 1024).toFixed(1)} MB`);
console.log(`Total despues: ${(totalAfter / 1024 / 1024).toFixed(1)} MB`);
console.log(`Reduccion: ${(100 - (totalAfter / totalBefore) * 100).toFixed(1)}%`);
