import re

# Read the HTML file
file_path = "/home/julian/diapos_control/Presentacion_Control_Biologico.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# --- 1. Replace empty span/icon elements with Material Symbols ---
replacements = {
    # Slide 2: Visual Icons
    r'<span class="visual-icon__icon"></span>\s*<span class="visual-icon__label">Enemigos naturales</span>': 
        '<span class="material-symbols-outlined visual-icon__icon" style="color:var(--primary); font-size: 2.2rem;">bug_report</span><span class="visual-icon__label">Enemigos naturales</span>',
    
    r'<span class="visual-icon__icon"></span>\s*<span class="visual-icon__label">Regulan plagas</span>': 
        '<span class="material-symbols-outlined visual-icon__icon" style="color:var(--primary); font-size: 2.2rem;">pest_control</span><span class="visual-icon__label">Regulan plagas</span>',
    
    r'<span class="visual-icon__icon"></span>\s*<span class="visual-icon__label">Sin químicos</span>': 
        '<span class="material-symbols-outlined visual-icon__icon" style="color:var(--primary); font-size: 2.2rem;">science_off</span><span class="visual-icon__label">Sin químicos</span>',
    
    r'<span class="visual-icon__icon"></span>\s*<span class="visual-icon__label">Equilibrio ecológico</span>': 
        '<span class="material-symbols-outlined visual-icon__icon" style="color:var(--primary); font-size: 2.2rem;">balance</span><span class="visual-icon__label">Equilibrio ecológico</span>',
    
    r'<span class="visual-icon__icon"></span>\s*<span class="visual-icon__label">Agricultura sostenible</span>': 
        '<span class="material-symbols-outlined visual-icon__icon" style="color:var(--primary); font-size: 2.2rem;">agriculture</span><span class="visual-icon__label">Agricultura sostenible</span>',

    # Slide 2: Diagram Nodes
    r'<div class="node"><span class="node-icon"></span>Plaga</div>':
        '<div class="node"><span class="material-symbols-outlined node-icon" style="vertical-align:middle; margin-right:4px;">bug_report</span>Plaga (Insecto malo)</div>',
    
    r'<div class="node"><span class="node-icon"></span>Enemigo Natural</div>':
        '<div class="node"><span class="material-symbols-outlined node-icon" style="vertical-align:middle; margin-right:4px;">shield</span>Enemigo Natural (El héroe)</div>',
    
    r'<div class="node"><span class="node-icon">️</span>Control</div>':
        '<div class="node"><span class="material-symbols-outlined node-icon" style="vertical-align:middle; margin-right:4px;">bolt</span>Control (Combate)</div>',
    
    r'<div class="node"><span class="node-icon"></span>Plaga Regulada</div>':
        '<div class="node"><span class="material-symbols-outlined node-icon" style="vertical-align:middle; margin-right:4px;">check_circle</span>Plaga Bajo Control</div>',

    # Slide 3: Checks
    r'<li><span class="check"></span>': '<li><span class="material-symbols-outlined" style="color:var(--green); font-size:1.1rem; vertical-align:middle; margin-right:4px;">check_circle</span>',
    r'<li><span class="check"></span>': '<li><span class="material-symbols-outlined" style="color:var(--green); font-size:1.1rem; vertical-align:middle; margin-right:4px;">check_circle</span>', # multiple passes handled

    # Slide 6: Ecosystem diagram nodes
    r'<div class="node"><span class="node-icon"></span>Planta</div>':
        '<div class="node"><span class="material-symbols-outlined node-icon" style="vertical-align:middle; margin-right:4px;">local_florist</span>Planta (Cultivo)</div>',
    r'<div class="node"><span class="node-icon"></span>Plaga</div>':
        '<div class="node"><span class="material-symbols-outlined node-icon" style="vertical-align:middle; margin-right:4px;">bug_report</span>Plaga</div>',
    r'<div class="node"><span class="node-icon"></span>Enemigo natural</div>':
        '<div class="node"><span class="material-symbols-outlined node-icon" style="vertical-align:middle; margin-right:4px;">shield</span>Enemigo natural</div>',
    r'<div class="node"><span class="node-icon"></span>Regulación</div>':
        '<div class="node"><span class="material-symbols-outlined node-icon" style="vertical-align:middle; margin-right:4px;">balance</span>Equilibrio ecológico</div>',

    # Slide 7: Tab Button icons
    r'<button class="tab-btn active" data-tab="clasico" onclick="switchTab\(\'clasico\'\)"><span style="font-size:1.1rem;margin-right:4px;"></span>':
        '<button class="tab-btn active" data-tab="clasico" onclick="switchTab(\'clasico\')"><span class="material-symbols-outlined" style="font-size:1.1rem;margin-right:4px;vertical-align:middle;">flight_land</span>',
    r'<button class="tab-btn" data-tab="aumentativo" onclick="switchTab\(\'aumentativo\'\)"><span style="font-size:1.1rem;margin-right:4px;"></span>':
        '<button class="tab-btn" data-tab="aumentativo" onclick="switchTab(\'aumentativo\')"><span class="material-symbols-outlined" style="font-size:1.1rem;margin-right:4px;vertical-align:middle;">group_add</span>',
    r'<button class="tab-btn" data-tab="conservacion" onclick="switchTab\(\'conservacion\'\)"><span style="font-size:1.1rem;margin-right:4px;"></span>':
        '<button class="tab-btn" data-tab="conservacion" onclick="switchTab(\'conservacion\')"><span class="material-symbols-outlined" style="font-size:1.1rem;margin-right:4px;vertical-align:middle;">yard</span>',

    # General list checks
    r'<span class="icon"></span>': '<span class="material-symbols-outlined" style="color:var(--green); font-size:1.1rem; vertical-align:middle; margin-right:4px;">check_circle</span>',
}

for src, dest in replacements.items():
    html = re.sub(src, dest, html)

# Replace all simple <span class="check"></span> that remain
html = html.replace('<span class="check"></span>', '<span class="material-symbols-outlined" style="color:var(--green); font-size:1.1rem; vertical-align:middle; margin-right:4px;">check_circle</span>')

# Let us fix the floating leaves to have Material Symbols inside
html = html.replace('<div class="floating-leaf floating-leaf-1"></div>', '<div class="floating-leaf floating-leaf-1"><span class="material-symbols-outlined" style="font-size: 2rem; color: var(--primary-light); opacity: 0.2;">eco</span></div>')
html = html.replace('<div class="floating-leaf floating-leaf-2"></div>', '<div class="floating-leaf floating-leaf-2"><span class="material-symbols-outlined" style="font-size: 1.5rem; color: var(--primary-light); opacity: 0.15;">yard</span></div>')
html = html.replace('<div class="floating-leaf floating-leaf-3"></div>', '<div class="floating-leaf floating-leaf-3"><span class="material-symbols-outlined" style="font-size: 2.5rem; color: var(--primary-light); opacity: 0.25;">nature</span></div>')
html = html.replace('<div class="floating-leaf floating-leaf-4"></div>', '<div class="floating-leaf floating-leaf-4"><span class="material-symbols-outlined" style="font-size: 1.8rem; color: var(--primary-light); opacity: 0.2;">eco</span></div>')

# --- 2. Simplify content for High Schoolers (10th/11th Grade) ---
# Replace scientific and highly technical texts with educational, interactive, and friendly terms

# Slide 1 Metadata
html = html.replace('<span> Investigación Académica</span>', '<span> Proyecto de Ciencias y Ecología</span>')
# Typing Text
html = html.replace('const text = \'Fundamentos, aplicaciones y perspectivas en la agricultura sostenible\';', 'const text = \'Aprende cómo la naturaleza defiende los cultivos de manera ecológica y sin químicos\';')

# Slide 2 Text Changes
html = html.replace(
    '<h2>¿Qué es el Control Biológico?</h2>',
    '<h2>¿Qué es el Control Biológico? (La Defensa Natural)</h2>'
)

# Slide 3 Text Changes
html = html.replace(
    '<h2>CB vs. Control Químico</h2>',
    '<h2>Control Biológico vs. Control Químico (Veneno)</h2>'
)
html = html.replace(
    '<h4> Control Biológico</h4>',
    '<h4> Control Biológico (Aliados de la Naturaleza)</h4>'
)
html = html.replace(
    '<h4>️ Control Químico</h4>',
    '<h4> Control Químico (Insecticidas Sintéticos)</h4>'
)

# Let us perform more edits to make text less heavy.
# Instead of replacing bit by bit, we can use regexes or load sections and rewrite.
# For example, let us look at Slide 8: Agentes de Control Biológico
# Mariquitas (Coccinellidae), Crisopas (Chrysopidae), Avispas (Hymenoptera)

# We will write the updated file
with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Icons replaced and base content updated!")
