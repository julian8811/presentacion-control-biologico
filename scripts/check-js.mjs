import { readFile, writeFile, mkdir } from "node:fs/promises";
import { execFile } from "node:child_process";
import { promisify } from "node:util";
import path from "node:path";
import os from "node:os";

const run = promisify(execFile);
const ROOT = path.resolve(import.meta.dirname, "..");
const html = await readFile(path.join(ROOT, "index.html"), "utf8");

const blocks = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map((m) => m[1]);
const tmp = path.join(os.tmpdir(), "presjs");
await mkdir(tmp, { recursive: true });

let ok = 0;
for (let i = 0; i < blocks.length; i++) {
  const f = path.join(tmp, `block${i}.js`);
  await writeFile(f, blocks[i], "utf8");
  try {
    await run(process.execPath, ["--check", f]);
    console.log(`Bloque ${i}: OK (${blocks[i].length} chars)`);
    ok++;
  } catch (e) {
    console.log(`Bloque ${i}: ERROR\n${e.stderr || e.message}`);
  }
}
console.log(`\n${ok}/${blocks.length} bloques de script sin errores de sintaxis`);
