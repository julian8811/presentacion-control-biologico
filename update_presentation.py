import sys

with open("Presentacion_Control_Biologico.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Slide 16 Background
slide_16_bg = """  <section class="slide" data-slide="16">
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-image: url('./el control biologico en colombia.jpeg'); background-size: cover; background-position: center; opacity: 0.15; z-index: 0; pointer-events: none;"></div>
    <div class="slide-content" style="position: relative; z-index: 1;">"""
content = content.replace('  <section class="slide" data-slide="16">\n    <div class="slide-content">', slide_16_bg)

# 2. Update Slide 16 Cards to be transparent
content = content.replace('<div class="card entrance-scale" style="background: white; border-radius: 16px; padding: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.04); text-align: center;">',
                          '<div class="card entrance-scale" style="background: rgba(255,255,255,0.9); backdrop-filter: blur(5px); border-radius: 16px; padding: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.04); text-align: center;">')
content = content.replace('<div class="card entrance-up" style="background: white; border-radius: 16px; padding: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.04); border-left: 4px solid var(--primary);">',
                          '<div class="card entrance-up" style="background: rgba(255,255,255,0.9); backdrop-filter: blur(5px); border-radius: 16px; padding: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.04); border-left: 4px solid var(--primary);">')
content = content.replace('<div style="grid-column: span 2; background: #fdfdfd; border-radius: 16px; padding: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); border: 1px solid #eee;">',
                          '<div style="grid-column: span 2; background: rgba(253,253,253,0.9); backdrop-filter: blur(5px); border-radius: 16px; padding: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); border: 1px solid #eee;">')
content = content.replace('<div style="background: #fdfdfd; border-radius: 16px; padding: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); border: 1px solid #eee;">\n            <h4 style="margin: 0 0 15px 0; font-size: 1.1rem; color: var(--text); display: flex; align-items: center; gap: 8px;"><span style="font-size: 1.3rem;"></span> Cultivos Principales</h4>',
                          '<div style="background: rgba(253,253,253,0.9); backdrop-filter: blur(5px); border-radius: 16px; padding: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); border: 1px solid #eee;">\n            <h4 style="margin: 0 0 15px 0; font-size: 1.1rem; color: var(--text); display: flex; align-items: center; gap: 8px;"><span style="font-size: 1.3rem;"></span> Cultivos Principales</h4>')
content = content.replace('<div style="background: #fdfdfd; border-radius: 16px; padding: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); border: 1px solid #eee;">\n            <h4 style="margin: 0 0 15px 0; font-size: 1.1rem; color: var(--text); display: flex; align-items: center; gap: 8px;"><span style="font-size: 1.3rem;"></span> Desafíos Reales</h4>',
                          '<div style="background: rgba(253,253,253,0.9); backdrop-filter: blur(5px); border-radius: 16px; padding: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); border: 1px solid #eee;">\n            <h4 style="margin: 0 0 15px 0; font-size: 1.1rem; color: var(--text); display: flex; align-items: center; gap: 8px;"><span style="font-size: 1.3rem;"></span> Desafíos Reales</h4>')

# 3. Add Slide 18
slide_18_html = """
  <!-- ===== SLIDE 18: Evaluación ===== -->
  <section class="slide" data-slide="18">
    <div class="slide-content" style="display: flex; flex-direction: column; height: 100%;">
      <h2 style="margin-bottom: 5px;">Evaluación de conocimientos</h2>
      <p style="text-align:center;font-size:0.85rem;color:var(--text-light);margin-bottom:20px;">Método científico y control biológico</p>
      
      <div style="flex: 1; overflow-y: auto; padding-right: 15px; margin-bottom: 20px;" class="custom-scrollbar">
        <div style="display: flex; flex-direction: column; gap: 15px;">
        
          <div class="card entrance-scale" style="background: rgba(255, 255, 255, 0.95); border-radius: 12px; padding: 20px; border-left: 4px solid var(--primary); box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <h4 style="margin: 0 0 15px 0; font-size: 1rem; color: var(--text);">1. Un agricultor nota que, en una esquina de su cultivo, las hormigas se están comiendo a los insectos pequeños que dañan sus plantas. ¿A qué paso del método científico corresponde lo que hizo el agricultor?</h4>
            <div style="display: flex; flex-direction: column; gap: 8px; font-size: 0.85rem; color: var(--text-light);">
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(45,106,79,0.1)'; this.style.color='var(--green-dark)';">(a) Observación</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(b) Experimentación</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(c) Sacar conclusiones</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(d) Formular una hipótesis</div>
            </div>
            <div style="display: none; margin-top: 15px; padding-top: 15px; border-top: 1px solid #eee;">
              <p style="font-size: 0.8rem; color: var(--green-dark); margin: 0;"><strong>Respuesta correcta: (a)</strong> Observación es el primer paso, donde se usa la vista y los sentidos para notar un hecho curioso en la naturaleza.</p>
            </div>
            <div style="margin-top: 15px; font-size: 0.8rem; color: var(--primary); font-weight: 600; cursor: pointer;" onclick="this.previousElementSibling.style.display = this.previousElementSibling.style.display === 'none' ? 'block' : 'none';">Ver justificación (Docente) ▼</div>
          </div>
          
          <div class="card entrance-scale" style="background: rgba(255, 255, 255, 0.95); border-radius: 12px; padding: 20px; border-left: 4px solid var(--primary); box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <h4 style="margin: 0 0 15px 0; font-size: 1rem; color: var(--text);">2. Un grupo de estudiantes dice: "Creemos que si sembramos plantas de olor fuerte cerca del tomate, los insectos plaga se irán por el aroma". Esta afirmación es:</h4>
            <div style="display: flex; flex-direction: column; gap: 8px; font-size: 0.85rem; color: var(--text-light);">
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(a) Una ley de la naturaleza</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(45,106,79,0.1)'; this.style.color='var(--green-dark)';">(b) Una hipótesis</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(c) Un resultado final</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(d) Un invento sin sentido</div>
            </div>
            <div style="display: none; margin-top: 15px; padding-top: 15px; border-top: 1px solid #eee;">
              <p style="font-size: 0.8rem; color: var(--green-dark); margin: 0;"><strong>Respuesta correcta: (b)</strong> Es una suposición o respuesta provisional que los estudiantes proponen y que todavía deben poner a prueba.</p>
            </div>
            <div style="margin-top: 15px; font-size: 0.8rem; color: var(--primary); font-weight: 600; cursor: pointer;" onclick="this.previousElementSibling.style.display = this.previousElementSibling.style.display === 'none' ? 'block' : 'none';">Ver justificación (Docente) ▼</div>
          </div>
          
          <div class="card entrance-scale" style="background: rgba(255, 255, 255, 0.95); border-radius: 12px; padding: 20px; border-left: 4px solid var(--primary); box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <h4 style="margin: 0 0 15px 0; font-size: 1rem; color: var(--text);">3. Para probar si un hongo bueno protege a las plantas de una enfermedad, un científico siembra 10 plantas CON el hongo bueno y otras 10 plantas SOLO con agua (sin el hongo). ¿Para qué sirven las 10 plantas que solo tienen agua?</h4>
            <div style="display: flex; flex-direction: column; gap: 8px; font-size: 0.85rem; color: var(--text-light);">
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(45,106,79,0.1)'; this.style.color='var(--green-dark)';">(a) Para comprobar qué pasa cuando no se aplica el tratamiento y poder comparar.</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(b) Para gastar menos hongo bueno en el experimento.</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(c) Para demostrar que el agua es mala para las plantas.</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(d) Para alterar los resultados si el hongo no funciona.</div>
            </div>
            <div style="display: none; margin-top: 15px; padding-top: 15px; border-top: 1px solid #eee;">
              <p style="font-size: 0.8rem; color: var(--green-dark); margin: 0;"><strong>Respuesta correcta: (a)</strong> Este grupo sirve como control o referencia para asegurar que los cambios se deben al hongo y no al azar.</p>
            </div>
            <div style="margin-top: 15px; font-size: 0.8rem; color: var(--primary); font-weight: 600; cursor: pointer;" onclick="this.previousElementSibling.style.display = this.previousElementSibling.style.display === 'none' ? 'block' : 'none';">Ver justificación (Docente) ▼</div>
          </div>
          
          <div class="card entrance-scale" style="background: rgba(255, 255, 255, 0.95); border-radius: 12px; padding: 20px; border-left: 4px solid var(--primary); box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <h4 style="margin: 0 0 15px 0; font-size: 1rem; color: var(--text);">4. Queremos investigar si la cantidad de luz solar (mucha, mediana o poca) cambia el tamaño de las hojas de una planta. En este experimento, ¿cuál es la variable que queremos medir (variable dependiente)?</h4>
            <div style="display: flex; flex-direction: column; gap: 8px; font-size: 0.85rem; color: var(--text-light);">
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(a) La cantidad de luz solar</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(45,106,79,0.1)'; this.style.color='var(--green-dark)';">(b) El tamaño de las hojas de la planta</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(c) El tipo de maceta</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(d) La cantidad de agua de riego</div>
            </div>
            <div style="display: none; margin-top: 15px; padding-top: 15px; border-top: 1px solid #eee;">
              <p style="font-size: 0.8rem; color: var(--green-dark); margin: 0;"><strong>Respuesta correcta: (b)</strong> El tamaño es la variable dependiente porque su valor 'depende' y cambia según la luz que reciba.</p>
            </div>
            <div style="margin-top: 15px; font-size: 0.8rem; color: var(--primary); font-weight: 600; cursor: pointer;" onclick="this.previousElementSibling.style.display = this.previousElementSibling.style.display === 'none' ? 'block' : 'none';">Ver justificación (Docente) ▼</div>
          </div>
          
          <div class="card entrance-scale" style="background: rgba(255, 255, 255, 0.95); border-radius: 12px; padding: 20px; border-left: 4px solid var(--primary); box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <h4 style="margin: 0 0 15px 0; font-size: 1rem; color: var(--text);">5. Si después de hacer un experimento con insectos descubres que tu idea inicial (hipótesis) estaba equivocada, ¿qué es lo correcto que debe hacer un científico?</h4>
            <div style="display: flex; flex-direction: column; gap: 8px; font-size: 0.85rem; color: var(--text-light);">
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(a) Cambiar las notas del experimento para que parezca que tenías la razón.</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(45,106,79,0.1)'; this.style.color='var(--green-dark)';">(b) Reconocerlo, cambiar la idea inicial y pensar en un nuevo experimento.</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(c) Dejar de investigar y decir que la ciencia no funciona.</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(d) Borrar todos los datos y no contarle a nadie lo que pasó.</div>
            </div>
            <div style="display: none; margin-top: 15px; padding-top: 15px; border-top: 1px solid #eee;">
              <p style="font-size: 0.8rem; color: var(--green-dark); margin: 0;"><strong>Respuesta correcta: (b)</strong> El método científico avanza aprendiendo de los errores y ajustando las ideas según la realidad observada.</p>
            </div>
            <div style="margin-top: 15px; font-size: 0.8rem; color: var(--primary); font-weight: 600; cursor: pointer;" onclick="this.previousElementSibling.style.display = this.previousElementSibling.style.display === 'none' ? 'block' : 'none';">Ver justificación (Docente) ▼</div>
          </div>
          
          <div class="card entrance-scale" style="background: rgba(255, 255, 255, 0.95); border-radius: 12px; padding: 20px; border-left: 4px solid var(--secondary); box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <h4 style="margin: 0 0 15px 0; font-size: 1rem; color: var(--text);">6. En lugar de usar venenos químicos artificiales que pueden contaminar el agua, algunos agricultores usan 'control biológico'. ¿A qué te suena que se refiere esto?</h4>
            <div style="display: flex; flex-direction: column; gap: 8px; font-size: 0.85rem; color: var(--text-light);">
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(a) A usar robots miniatura para atrapar insectos uno a uno.</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(45,106,79,0.1)'; this.style.color='var(--green-dark)';">(b) A aprovechar seres vivos (como insectos buenos, hongos o bacterias) para controlar a las plagas dañinas.</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(c) A dejar que la plaga se coma todo el cultivo sin hacer nada.</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(d) A usar más fertilizantes químicos para que la planta crezca rápido.</div>
            </div>
            <div style="display: none; margin-top: 15px; padding-top: 15px; border-top: 1px solid #eee;">
              <p style="font-size: 0.8rem; color: var(--green-dark); margin: 0;"><strong>Respuesta correcta: (b)</strong> El control biológico utiliza las relaciones naturales de los seres vivos para mantener el equilibrio en los cultivos.</p>
            </div>
            <div style="margin-top: 15px; font-size: 0.8rem; color: var(--primary); font-weight: 600; cursor: pointer;" onclick="this.previousElementSibling.style.display = this.previousElementSibling.style.display === 'none' ? 'block' : 'none';">Ver justificación (Docente) ▼</div>
          </div>
          
          <div class="card entrance-scale" style="background: rgba(255, 255, 255, 0.95); border-radius: 12px; padding: 20px; border-left: 4px solid var(--secondary); box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <h4 style="margin: 0 0 15px 0; font-size: 1rem; color: var(--text);">7. Las mariquitas o catarinas son pequeños escarabajos que buscan activamente y se comen a los pulgones (unos insectos diminutos que marchitan las hojas). ¿Qué tipo de relación hay aquí?</h4>
            <div style="display: flex; flex-direction: column; gap: 8px; font-size: 0.85rem; color: var(--text-light);">
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(45,106,79,0.1)'; this.style.color='var(--green-dark)';">(a) Depredación (un ser vivo caza y se come a otro)</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(b) Amistad o colaboración</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(c) Competencia por la luz del sol</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(d) Enfermedad</div>
            </div>
            <div style="display: none; margin-top: 15px; padding-top: 15px; border-top: 1px solid #eee;">
              <p style="font-size: 0.8rem; color: var(--green-dark); margin: 0;"><strong>Respuesta correcta: (a)</strong> La mariquita actúa como un cazador o depredador directo de su presa, que es el pulgón.</p>
            </div>
            <div style="margin-top: 15px; font-size: 0.8rem; color: var(--primary); font-weight: 600; cursor: pointer;" onclick="this.previousElementSibling.style.display = this.previousElementSibling.style.display === 'none' ? 'block' : 'none';">Ver justificación (Docente) ▼</div>
          </div>
          
          <div class="card entrance-scale" style="background: rgba(255, 255, 255, 0.95); border-radius: 12px; padding: 20px; border-left: 4px solid var(--secondary); box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <h4 style="margin: 0 0 15px 0; font-size: 1rem; color: var(--text);">8. Imaginen que un hongo microscópico muy bueno se siembra en la raíz de una planta y ocupa todo el espacio, evitando que los hongos malos lleguen a enfermarla. ¿Cómo logra este hongo bueno proteger a la planta?</h4>
            <div style="display: flex; flex-direction: column; gap: 8px; font-size: 0.85rem; color: var(--text-light);">
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(a) Abriendo caminos ocultos bajo la tierra.</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(45,106,79,0.1)'; this.style.color='var(--green-dark)';">(b) Compitiendo por el espacio y la vivienda para que el malo no encuentre lugar.</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(c) Asustando al hongo malo con ruidos extraños.</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(d) Haciendo que la planta crezca al revés.</div>
            </div>
            <div style="display: none; margin-top: 15px; padding-top: 15px; border-top: 1px solid #eee;">
              <p style="font-size: 0.8rem; color: var(--green-dark); margin: 0;"><strong>Respuesta correcta: (b)</strong> Al ocupar primero el lugar disponible, el organismo benéfico le quita el espacio y los nutrientes al patógeno.</p>
            </div>
            <div style="margin-top: 15px; font-size: 0.8rem; color: var(--primary); font-weight: 600; cursor: pointer;" onclick="this.previousElementSibling.style.display = this.previousElementSibling.style.display === 'none' ? 'block' : 'none';">Ver justificación (Docente) ▼</div>
          </div>
          
          <div class="card entrance-scale" style="background: rgba(255, 255, 255, 0.95); border-radius: 12px; padding: 20px; border-left: 4px solid var(--secondary); box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <h4 style="margin: 0 0 15px 0; font-size: 1rem; color: var(--text);">9. Si un agricultor usa el mismo veneno químico durante muchos años seguidos, al final los insectos malos se acostumbran y ya no mueren (se vuelven resistentes). Si queremos investigar una solución ecológica para esto, ¿cuál sería una buena pregunta para empezar?</h4>
            <div style="display: flex; flex-direction: column; gap: 8px; font-size: 0.85rem; color: var(--text-light);">
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(a) ¿Cómo podemos fabricar un veneno químico diez veces más fuerte?</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(45,106,79,0.1)'; this.style.color='var(--green-dark)';">(b) ¿Podrá un insecto bueno de la región ayudarnos a reducir la población de esta plaga de forma natural?</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(c) ¿Cuánto cuesta comprar un tractor nuevo?</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(d) ¿Por qué los insectos tienen seis patas?</div>
            </div>
            <div style="display: none; margin-top: 15px; padding-top: 15px; border-top: 1px solid #eee;">
              <p style="font-size: 0.8rem; color: var(--green-dark); margin: 0;"><strong>Respuesta correcta: (b)</strong> La pregunta debe enfocarse en buscar una alternativa natural y viva para solucionar el fallo del veneno químico.</p>
            </div>
            <div style="margin-top: 15px; font-size: 0.8rem; color: var(--primary); font-weight: 600; cursor: pointer;" onclick="this.previousElementSibling.style.display = this.previousElementSibling.style.display === 'none' ? 'block' : 'none';">Ver justificación (Docente) ▼</div>
          </div>
          
          <div class="card entrance-scale" style="background: rgba(255, 255, 255, 0.95); border-radius: 12px; padding: 20px; border-left: 4px solid var(--secondary); box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <h4 style="margin: 0 0 15px 0; font-size: 1rem; color: var(--text);">10. Después de contar los insectos que quedaron en nuestro experimento, organizamos los números en una gráfica de barras de colores para ver más fácil si el tratamiento funcionó. ¿En qué momento del método científico hacemos esto?</h4>
            <div style="display: flex; flex-direction: column; gap: 8px; font-size: 0.85rem; color: var(--text-light);">
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(45,106,79,0.1)'; this.style.color='var(--green-dark)';">(a) En el análisis de los resultados</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(b) Al inicio, antes de sembrar las plantas</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(c) Al momento de elegir el nombre del proyecto</div>
              <div style="padding: 8px 12px; background: rgba(0,0,0,0.03); border-radius: 8px; cursor: pointer;" onclick="this.style.background='rgba(231,76,60,0.1)'; this.style.color='#c0392b';">(d) Cuando decidimos no hacer el experimento</div>
            </div>
            <div style="display: none; margin-top: 15px; padding-top: 15px; border-top: 1px solid #eee;">
              <p style="font-size: 0.8rem; color: var(--green-dark); margin: 0;"><strong>Respuesta correcta: (a)</strong> Hacer dibujos, tablas y gráficas con los números obtenidos sirve para entender qué nos dijeron los experimentos.</p>
            </div>
            <div style="margin-top: 15px; font-size: 0.8rem; color: var(--primary); font-weight: 600; cursor: pointer;" onclick="this.previousElementSibling.style.display = this.previousElementSibling.style.display === 'none' ? 'block' : 'none';">Ver justificación (Docente) ▼</div>
          </div>

        </div>
      </div>
    </div>
    <span class="slide-number">18 / 18</span>
  </section>
"""
content = content.replace('<!-- ===== Navigation Bar ===== -->', slide_18_html + '\n</div>\n\n<!-- ===== Navigation Bar ===== -->')

# 4. Update JavaScript to support Slide 18
content = content.replace('totalSlides: 17,', 'totalSlides: 18,')
content = content.replace('<span class="progress-text" id="progressText">1/17</span>', '<span class="progress-text" id="progressText">1/18</span>')
content = content.replace('<p>17 diapositivas</p>', '<p>18 diapositivas</p>')
sidebar_18 = '            <li><a class="sidebar-link" data-slide-link="17" onclick="goToSlide(17);toggleSidebar()"><span class="link-num">17</span> Referencias</a></li>\n            <li><a class="sidebar-link" data-slide-link="18" onclick="goToSlide(18);toggleSidebar()"><span class="link-num">18</span> Evaluación</a></li>'
content = content.replace('            <li><a class="sidebar-link" data-slide-link="17" onclick="goToSlide(17);toggleSidebar()"><span class="link-num">17</span> Referencias</a></li>', sidebar_18)

with open("Presentacion_Control_Biologico.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done!")
