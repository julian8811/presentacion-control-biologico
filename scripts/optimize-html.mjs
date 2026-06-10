import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";

const ROOT = path.resolve(import.meta.dirname, "..");
const HTML = path.join(ROOT, "index.html");
const PLACEHOLDER =
  "data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==";

let html = await readFile(HTML, "utf8");
let imgCount = 0;
let videoCount = 0;
let bgCount = 0;

// 1) Imagenes de contenido -> carga diferida con data-src
html = html.replace(/<img\b[^>]*>/g, (tag) => {
  if (/data-src=/.test(tag)) return tag;
  const m = tag.match(/\ssrc=("|')(\.\/[^"']+)\1/);
  if (!m) return tag; // imgs sin src local (modal) se dejan igual
  imgCount++;
  return tag
    .replace(/\ssrc=("|')\.\/[^"']+\1/, ` src="${PLACEHOLDER}" data-src="${m[2]}"`)
    .replace(/<img\b/, '<img class="lazy-media"');
});

// 2) Videos -> carga diferida y reproduccion solo en slide activa
html = html.replace(
  /<video\s+src=("|')(\.\/[^"']+\.mp4)\1\s+autoplay\s+loop\s+muted\s+playsinline/g,
  (_match, _q, src) => {
    videoCount++;
    return `<video data-vsrc="${src}" loop muted playsinline preload="none"`;
  },
);
html = html.split("openImageModal(this.src, true)").join("openImageModal(this.dataset.vsrc, true)");

// 3) Fondos decorativos inline -> data-bg
html = html.replace(
  /<div style="([^"]*?)background-image:\s*url\('([^']+)'\);\s*([^"]*?)">/g,
  (_match, pre, url, post) => {
    bgCount++;
    return `<div data-bg="${url}" style="${pre}${post}">`;
  },
);

// 4) Hook de carga en goToSlide
html = html.replace(
  "  next.classList.add('active');\n  state.currentSlide = n;",
  "  next.classList.add('active');\n  state.currentSlide = n;\n  __activateSlideMedia(next, current);",
);

// 5) Funciones de carga diferida + init
const lazyJs = `/* ===== Lazy media (carga por slide) ===== */
function __loadMediaIn(slide){
  if(!slide) return;
  slide.querySelectorAll('img[data-src]').forEach(function(img){ img.src=img.getAttribute('data-src'); img.removeAttribute('data-src'); });
  slide.querySelectorAll('[data-bg]').forEach(function(el){ el.style.backgroundImage="url('"+el.getAttribute('data-bg')+"')"; el.removeAttribute('data-bg'); });
  slide.querySelectorAll('video[data-vsrc]').forEach(function(v){ v.src=v.getAttribute('data-vsrc'); v.removeAttribute('data-vsrc'); v.load(); });
}
function __playMediaIn(slide, play){
  if(!slide) return;
  slide.querySelectorAll('video').forEach(function(v){ if(play){ var p=v.play(); if(p&&p.catch)p.catch(function(){}); } else { try{v.pause();}catch(e){} } });
}
function __activateSlideMedia(next, current){
  if(!next) return;
  __loadMediaIn(next);
  var n = parseInt(next.dataset.slide);
  __loadMediaIn(document.querySelector('.slide[data-slide="'+(n+1)+'"]'));
  __playMediaIn(current, false);
  __playMediaIn(next, true);
}

/* ===== Init ===== */`;

html = html.replace("/* ===== Init ===== */", lazyJs);

html = html.replace(
  "  initCycleObserver();\n  initTypingEffect();\n  updateTimelineProgress();\n});",
  `  initCycleObserver();
  initTypingEffect();
  updateTimelineProgress();
  var __first = document.querySelector('.slide[data-slide="1"]');
  __loadMediaIn(__first);
  __loadMediaIn(document.querySelector('.slide[data-slide="2"]'));
  __playMediaIn(__first, true);
});`,
);

await writeFile(HTML, html, "utf8");
console.log(`Imagenes diferidas: ${imgCount}`);
console.log(`Videos diferidos: ${videoCount}`);
console.log(`Fondos diferidos: ${bgCount}`);
