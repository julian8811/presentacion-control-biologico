import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";

const HTML = path.join(path.resolve(import.meta.dirname, ".."), "index.html");
let html = await readFile(HTML, "utf8");

/** @type {[string|string, string][]} */
const pairs = [
  // Ortografía y clic
  ["Haz click", "Haz clic"],
  ["haz click", "haz clic"],

  // Portada
  [
    "Aprende cómo la naturaleza defiende los cultivos de manera ecológica y sin químicos",
    "Descubre cómo la naturaleza protege los cultivos de forma ecológica, sin depender de químicos",
  ],

  // Slide 2
  [
    "Usar la fuerza de la naturaleza para proteger tus alimentos.",
    "Aprovechar la capacidad de la naturaleza para proteger los cultivos y los alimentos.",
  ],
  [
    "En lugar de rociar los campos con venenos químicos, invitamos a los <strong>enemigos naturales</strong> de las plagas (insectos buenos, ácaros o microorganismos) a hacer el trabajo sucio. Ellos cazan, enferman o controlan a los insectos dañinos de forma natural.",
    "En lugar de depender de plaguicidas sintéticos, se favorece la acción de los <strong>enemigos naturales</strong> de las plagas —insectos, ácaros u hongos benéficos— que cazan, parasitan o enferman a los insectos dañinos.",
  ],

  // Slide 3
  [
    "<strong>Dato curioso:</strong> ¡Los insectos se adaptan al veneno químico como los jefes de tus videojuegos! Se vuelven inmunes y necesitas químicos más fuertes. Con el control biológico esto no pasa porque el depredador también evoluciona para seguir cazándolos.",
    "<strong>Dato clave:</strong> Con los insecticidas, las plagas pueden volverse resistentes y exigir productos cada vez más fuertes. En el control biológico, depredadores y parasitoides también se adaptan, lo que dificulta que la plaga escape del equilibrio natural.",
  ],

  // Slide 4
  [
    "Pilar fundamental del Manejo Integrado de Plagas (MIP): El Plan de Defensa Integral (MIP)",
    "Pilar del Manejo Integrado de Plagas (MIP): un plan que combina monitoreo, prevención y control",
  ],
  [
    "Los bichos buenos respetan a las abejas y mariposas.",
    "Los organismos benéficos suelen ser más selectivos y respetan a abejas y mariposas.",
  ],
  [
    "El campo se defiende solo, reduciendo los costos de mantenimiento.",
    "El cultivo se regula con menos intervenciones, lo que reduce costos de mantenimiento.",
  ],

  // Slide 5
  [
    "Desde la antigua China hasta la era de la inteligencia artificial. <strong>Haz clic en cada época</strong> para explorarla.",
    "Desde la antigua China hasta la era de la inteligencia artificial. <strong>Haz clic en cada hito</strong> para conocerlo.",
  ],
  [
    '<div style="font-size: 0.85rem; font-weight: 600;">Rodolia cardinalis</div>',
    '<div style="font-size: 0.85rem; font-weight: 600;"><em>Rodolia cardinalis</em></div>',
  ],

  // Slide 6
  [
    "El depredador se alimenta de la presa. Ambas poblaciones mantienen un equilibrio natural acoplado.",
    "El depredador se alimenta de la presa y ambas poblaciones se regulan mutuamente en el tiempo.",
  ],
  [
    "Se desarrollan sobre o dentro de un hospedero específico, provocando su muerte. Alta especificidad.",
    "Se desarrollan sobre o dentro de un hospedero concreto y suelen matarlo. Por eso son muy específicos.",
  ],

  // Slide 7
  [
    "donde una plaga,generalmente también exótica",
    "donde una plaga, generalmente también exótica",
  ],
  [
    "Ej: <em>Encarsia formosa</em>",
    "Ejemplo: <em>Encarsia formosa</em>",
  ],
  [
    "Ej: <em>Trichogramma</em> spp.",
    "Ejemplo: <em>Trichogramma</em> spp.",
  ],

  // Slide 8
  [
    "<h2>Nuestros aliados: los bichos buenos</h2>",
    "<h2>Nuestros aliados: organismos benéficos</h2>",
  ],
  [
    "<h4 style=\"color: #c0392b; font-size: 1.15rem; margin-top:0; margin-bottom: 8px;\">2. Avispas Parasitoides (Los Aliens)</h4>",
    "<h4 style=\"color: #c0392b; font-size: 1.15rem; margin-top:0; margin-bottom: 8px;\">2. Avispas parasitoides</h4>",
  ],
  [
    "<strong>Dato curioso:</strong> Estas avispitas inspiraron la película <em>Alien</em>. Ponen sus huevos dentro de insectos plaga. Al nacer, sus larvas se comen al huésped por dentro con precisión quirúrgica, operando por <strong>parasitismo</strong>.",
    "Las hembras depositan huevos dentro del insecto plaga. Sus larvas se desarrollan consumiendo los tejidos del huésped, un mecanismo de <strong>parasitismo</strong> muy eficaz y específico.",
  ],

  // Slide 9
  [
    "Penetración cuticular e intestinal. Hongos, bacterias (como Bt), baculovirus o nematodos colonizan al insecto causando septicemia letal.",
    "Penetración cuticular o intestinal. Hongos, bacterias como <em>Bacillus thuringiensis</em> (Bt), baculovirus o nematodos colonizan al insecto y pueden causar su muerte.",
  ],
  [
    "Secreción de sustancias tóxicas especializadas (beauvericina, destruxinas, proteínas Cry) que paralizan rápidamente al huésped.",
    "Producción de metabolitos tóxicos (beauvericina, destruxinas, proteínas Cry) que debilitan o matan al huésped.",
  ],

  // Slide 10
  [
    "<h2>Hongos zombie (armas biológicas naturales)</h2>",
    "<h2>Hongos entomopatógenos: defensa microscópica</h2>",
  ],
  [
    "<strong> Dato curioso:</strong> ¡Es el equivalente literal a un apocalipsis zombie para los insectos plaga!",
    "<strong>Dato clave:</strong> El hongo transforma al insecto en un «vehículo» que dispersa nuevas esporas, amplificando el control en el campo.",
  ],

  // Tarjetas de cultivos — plagas y agentes
  [
    '<div style="font-size: 0.75rem; color: var(--text-light); font-style: italic; line-height:1.3;">Bemisia tabaci (Mosca blanca)</div>',
    '<div style="font-size: 0.75rem; color: var(--text-light); line-height:1.3;"><em>Bemisia tabaci</em> (mosca blanca)</div>',
  ],
  [
    '<div style="font-size: 0.85rem; font-weight: 600; margin-top: auto; padding-top: 8px; border-top: 1px solid #f0f0f0; color: var(--primary);">Encarsia formosa</div>',
    '<div style="font-size: 0.85rem; font-weight: 600; margin-top: auto; padding-top: 8px; border-top: 1px solid #f0f0f0; color: var(--primary);"><em>Encarsia formosa</em></div>',
  ],
  [
    '<div style="font-size: 0.75rem; color: var(--text-light); font-style: italic; line-height:1.3;">Spodoptera frugiperda</div>',
    '<div style="font-size: 0.75rem; color: var(--text-light); line-height:1.3;"><em>Spodoptera frugiperda</em></div>',
  ],
  [
    '<div style="font-size: 0.85rem; font-weight: 600; margin-top: auto; padding-top: 8px; border-top: 1px solid #f0f0f0; color: var(--primary);">Bacillus thuringiensis (Bt)</div>',
    '<div style="font-size: 0.85rem; font-weight: 600; margin-top: auto; padding-top: 8px; border-top: 1px solid #f0f0f0; color: var(--primary);"><em>Bacillus thuringiensis</em> (Bt)</div>',
  ],
  [
    '<div style="font-size: 0.75rem; color: var(--text-light); font-style: italic; line-height:1.3;">Hypothenemus hampei (Broca)</div>',
    '<div style="font-size: 0.75rem; color: var(--text-light); line-height:1.3;"><em>Hypothenemus hampei</em> (broca del café)</div>',
  ],
  [
    '<div style="font-size: 0.85rem; font-weight: 600; margin-top: auto; padding-top: 8px; border-top: 1px solid #f0f0f0; color: var(--primary);">Beauveria bassiana</div>',
    '<div style="font-size: 0.85rem; font-weight: 600; margin-top: auto; padding-top: 8px; border-top: 1px solid #f0f0f0; color: var(--primary);"><em>Beauveria bassiana</em></div>',
  ],
  [
    '<div style="font-size: 0.85rem; font-weight: 600; margin-top: auto; padding-top: 8px; border-top: 1px solid #f0f0f0; color: var(--primary);">Rodolia cardinalis</div>',
    '<div style="font-size: 0.85rem; font-weight: 600; margin-top: auto; padding-top: 8px; border-top: 1px solid #f0f0f0; color: var(--primary);"><em>Rodolia cardinalis</em></div>',
  ],
  [
    '<div style="font-size: 0.85rem; font-weight: 600; margin-top: auto; padding-top: 8px; border-top: 1px solid #f0f0f0; color: var(--primary);">Phytoseiulus persimilis</div>',
    '<div style="font-size: 0.85rem; font-weight: 600; margin-top: auto; padding-top: 8px; border-top: 1px solid #f0f0f0; color: var(--primary);"><em>Phytoseiulus persimilis</em></div>',
  ],
  [
    '<div style="font-size: 0.75rem; color: var(--text-light); font-style: italic; line-height:1.3;">Cosmopolites sordidus</div>',
    '<div style="font-size: 0.75rem; color: var(--text-light); line-height:1.3;"><em>Cosmopolites sordidus</em></div>',
  ],
  [
    '<div style="font-size: 0.85rem; font-weight: 600; margin-top: auto; padding-top: 8px; border-top: 1px solid #f0f0f0; color: var(--primary);">B. bassiana, Steinernema</div>',
    '<div style="font-size: 0.85rem; font-weight: 600; margin-top: auto; padding-top: 8px; border-top: 1px solid #f0f0f0; color: var(--primary);"><em>B. bassiana</em>, <em>Steinernema</em> spp.</div>',
  ],

  // Timeline JS
  [
    "title: 'Rodolia cardinalis en California'",
    "title: '<em>Rodolia cardinalis</em> en California'",
  ],
  [
    "desc: 'La mariquita <em>Rodolia cardinalis</em> controló",
    "desc: 'La mariquita <em>R. cardinalis</em> controló",
  ],

  // Referencias
  [
    "Mode of action of Bacillus thuringiensis Cry and Cyt toxins.",
    "Mode of action of <em>Bacillus thuringiensis</em> Cry and Cyt toxins.",
  ],

  // Quiz explanation
  [
    "explanation.textContent = 'La liberación de Encarsia formosa (parasitoide especializado de mosca blanca)",
    "explanation.textContent = 'La liberación de Encarsia formosa (parasitoide de mosca blanca)",
  ],

  // Riesgos
  [
    "para controlar la polilla gitana, terminó parasitando",
    "para controlar la polilla gitana (<em>Lymantria dispar</em>), terminó parasitando",
  ],

  // MIP
  [
    "Colocar trampas y revisar las hojas para contar cuántos insectos buenos y malos hay antes de tomar decisiones.",
    "Usar trampas y muestreos para estimar la abundancia de plagas y de enemigos naturales antes de intervenir.",
  ],
  [
    "Punto donde hay tantas plagas que si no actuamos perderemos dinero, pero vigilando antes de que ocurra.",
    "Umbral en el que conviene actuar para evitar daños económicos, detectado gracias al monitoreo previo.",
  ],
];

let n = 0;
for (const [from, to] of pairs) {
  if (!html.includes(from)) {
    console.warn("No encontrado:", from.slice(0, 60) + "...");
    continue;
  }
  html = html.split(from).join(to);
  n++;
}
console.log(`Reemplazos aplicados: ${n}/${pairs.length}`);

// CSS para nombres científicos en citas
if (!html.includes(".sci-name")) {
  html = html.replace(
    "p  { font-family: var(--font-body);",
    "em.sci-name, .sci-name { font-style: italic; }\np  { font-family: var(--font-body);",
  );
}

await writeFile(HTML, html, "utf8");
