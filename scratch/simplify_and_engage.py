import re

file_path = "/home/julian/diapos_control/Presentacion_Control_Biologico.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let us do a targeted python replacement for all slide contents to make them extremely punchy,
# free of academic jargon, concrete, and packed with hook facts (datos curiosos).

# 1. Slide 2: ¿Qué es el Control Biológico?
slide2_old = re.search(r'(<section class="slide" data-slide="2">.*?</section>)', content, re.DOTALL)
slide2_new = """<section class="slide" data-slide="2">
    <div class="slide-content">
      <h2>¿Qué es el Control Biológico?</h2>
      <p class="subtitle" style="font-size: 1.1rem; color: var(--primary); font-weight: 600; margin-bottom: 20px;">
        Usar la fuerza de la naturaleza para proteger tus alimentos.
      </p>
      <div class="card" style="padding: 24px; margin-bottom: 20px;">
        <h4 style="color: var(--primary); margin-bottom: 12px; font-size: 1.2rem;">La regla de oro: El enemigo de mi enemigo es mi amigo</h4>
        <p style="font-size: 1rem; line-height: 1.6;">
          En lugar de rociar los campos con venenos químicos, invitamos a los <strong>enemigos naturales</strong> de las plagas (insectos buenos, ácaros o microorganismos) a hacer el trabajo sucio. Ellos cazan, enferman o controlan a los insectos dañinos de forma natural.
        </p>
      </div>
      <div class="diagram-flow-h entrance-left" style="margin-bottom: 14px; gap: 8px;">
        <div class="node"><span class="material-symbols-outlined" style="vertical-align:middle; margin-right:4px;">bug_report</span>Plaga (El villano)</div>
        <span class="arrow">→</span>
        <div class="node"><span class="material-symbols-outlined" style="vertical-align:middle; margin-right:4px;">shield</span>Enemigo Natural (El héroe)</div>
        <span class="arrow">→</span>
        <div class="node"><span class="material-symbols-outlined" style="vertical-align:middle; margin-right:4px;">bolt</span>Combate Natural</div>
        <span class="arrow">→</span>
        <div class="node"><span class="material-symbols-outlined" style="vertical-align:middle; margin-right:4px;">check_circle</span>Cultivo a Salvo</div>
      </div>
    </div>
    <span class="slide-number">2 / 19</span>
  </section>"""

if slide2_old:
    content = content.replace(slide2_old.group(1), slide2_new)

# 2. Slide 3: CB vs. Químico
slide3_old = re.search(r'(<section class="slide" data-slide="3">.*?</section>)', content, re.DOTALL)
slide3_new = """<section class="slide" data-slide="3">
    <div class="slide-content">
      <h2>Control Biológico vs. Control Químico (Venenos)</h2>
      <div class="comparison-card entrance-right" style="margin-top:4px;">
        <div class="comparison-col bio">
          <h4> Control Biológico (Seguro y Ecológico)</h4>
          <ul>
            <li><span class="material-symbols-outlined" style="color:var(--green); font-size:1.1rem; vertical-align:middle; margin-right:4px;">check_circle</span> No contamina el suelo, el agua ni la comida</li>
            <li><span class="material-symbols-outlined" style="color:var(--green); font-size:1.1rem; vertical-align:middle; margin-right:4px;">check_circle</span> Los insectos malos no se vuelven inmunes</li>
            <li><span class="material-symbols-outlined" style="color:var(--green); font-size:1.1rem; vertical-align:middle; margin-right:4px;">check_circle</span> Solo ataca al insecto malo (respeta abejas y mariposas)</li>
          </ul>
        </div>
        <div class="comparison-col quimico">
          <h4> Control Químico (Insecticidas Artificiales)</h4>
          <ul>
            <li><span class="material-symbols-outlined" style="color:var(--error); font-size:1.1rem; vertical-align:middle; margin-right:4px;">cancel</span> Deja veneno en los alimentos y mata abejas</li>
            <li><span class="material-symbols-outlined" style="color:var(--error); font-size:1.1rem; vertical-align:middle; margin-right:4px;">cancel</span> Crea superplagas resistentes muy rápido</li>
            <li><span class="material-symbols-outlined" style="color:var(--error); font-size:1.1rem; vertical-align:middle; margin-right:4px;">cancel</span> Requiere aplicar veneno una y otra vez</li>
          </ul>
        </div>
      </div>
      <div class="card" style="margin-top: 15px; padding: 16px; border-left: 4px solid var(--tertiary);">
        <p style="margin: 0; font-size: 0.95rem;">
          <strong>Dato curioso:</strong> ¡Los insectos se adaptan al veneno químico como los jefes de tus videojuegos! Se vuelven inmunes y necesitas químicos más fuertes. Con el control biológico esto no pasa porque el depredador también evoluciona para seguir cazándolos.
        </p>
      </div>
    </div>
    <span class="slide-number">3 / 19</span>
  </section>"""

if slide3_old:
    content = content.replace(slide3_old.group(1), slide3_new)

# 3. Slide 8: Aliados
slide8_old = re.search(r'(<section class="slide" data-slide="8">.*?</section>)', content, re.DOTALL)
slide8_new = """<section class="slide" data-slide="8">
    <div class="slide-content">
      <h2>Nuestros Aliados: Los Bichos Buenos</h2>
      <p class="subtitle" style="font-size: 1rem; margin-bottom: 20px;">Conoce a los depredadores y los parasitoides.</p>
      <div style="display: grid; grid-template-cols: 1fr; gap: 16px;">
        <div class="card" style="padding: 16px; border-left: 4px solid var(--primary);">
          <h4 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 8px;">1. Las Mariquitas: Las devoradoras voraces</h4>
          <p style="font-size: 0.9rem; margin-bottom: 6px;">
            No te dejes engañar por su aspecto tierno. Una sola mariquita puede comerse hasta <strong>5,000 pulgones</strong> en su vida. Son máquinas de cazar plagas desde que son bebés (larvas).
          </p>
        </div>
        <div class="card" style="padding: 16px; border-left: 4px solid var(--tertiary);">
          <h4 style="color: var(--tertiary-container); font-size: 1.1rem; margin-bottom: 8px;">2. Las Avispas Parasitoides: Las Aliens reales</h4>
          <p style="font-size: 0.9rem; margin-bottom: 6px;">
            <strong>Dato curioso:</strong> Estas avispitas inspiraron la famosa película <em>Alien</em>. Ponen sus huevos dentro de otros insectos plaga. Al nacer, sus larvas se comen al huésped por dentro con precisión quirúrgica sin dañar al resto del cultivo.
          </p>
        </div>
      </div>
    </div>
    <span class="slide-number">8 / 19</span>
  </section>"""

if slide8_old:
    content = content.replace(slide8_old.group(1), slide8_new)

# 4. Slide 10: Fungi Zombie
slide10_old = re.search(r'(<section class="slide" data-slide="10">.*?</section>)', content, re.DOTALL)
slide10_new = """<section class="slide" data-slide="10">
    <div class="slide-content">
      <h2>Hongos Zombie (Armas biológicas naturales)</h2>
      <div class="card" style="padding: 24px; margin-bottom: 16px; border-left: 4px solid var(--error);">
        <h4 style="color: var(--error); margin-bottom: 10px; font-size: 1.15rem;">El Hongo Beauveria: La pesadilla de los bichos malos</h4>
        <p style="font-size: 0.95rem; line-height: 1.6; margin-bottom: 12px;">
          Existen hongos buenos (como <em>Beauveria bassiana</em>) que lanzan esporas invisibles en el aire. Cuando tocan a un insecto plaga, el hongo entra por su piel, invade su cuerpo por dentro y lo convierte en una estatua momificada cubierta de polvo blanco.
        </p>
        <p style="font-size: 0.95rem; font-weight: 600; margin: 0; color: var(--primary-light);">
          <strong>Dato curioso:</strong> ¡Es el equivalente real a un apocalipsis zombie para los insectos plaga!
        </p>
      </div>
    </div>
    <span class="slide-number">10 / 19</span>
  </section>"""

if slide10_old:
    content = content.replace(slide10_old.group(1), slide10_new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Targeted slides redesigned for high-schoolers with shocking facts and concrete content!")
