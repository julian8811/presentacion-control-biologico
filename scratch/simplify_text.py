import re

file_path = "/home/julian/diapos_control/Presentacion_Control_Biologico.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replacements to make presentation friendly for 10th & 11th grade students:
text_replacements = {
    # General Slide Titles / Subtitles
    "¿Qué es el Control Biológico?": "¿Qué es el Control Biológico? 🐛",
    "CB vs. Control Químico": "Control Biológico vs. Control Químico (Insecticidas) 🧪",
    "Fundamentos Ecológicos": "Fundamentos Ecológicos (Cómo funciona la naturaleza) 🌳",
    "Tipos de Control Biológico": "Tipos de Control Biológico (Las Estrategias) 🎯",
    "Agentes de Control Biológico": "Nuestros Aliados: Los Agentes de Control Biológico 🐞",
    "Mecanismos de Acción": "Mecanismos de Acción (¿Cómo atacan a las plagas?) ⚡",
    "Hongos Entomopatógenos": "Hongos que enferman insectos plaga (Entomopatógenos) 🍄",
    "Aplicaciones Agrícolas": "Aplicaciones en el Campo (Casos Reales) 🌾",
    "Manejo Integrado de Plagas": "Manejo Integrado de Plagas (MIP): El Plan de Defensa Integral 🛡️",
    "Ventajas y Limitaciones": "Lo Bueno y lo Desafiante (Ventajas y Límites) ⚖️",
    "Riesgos y Consideraciones Éticas": "Cuidado: Riesgos y Consideraciones Éticas ⚠️",
    "Tendencias e Innovaciones": "El Futuro del Control Biológico (Drones e IA) 🚀",
    "Colombia y América Latina": "El Control Biológico en Colombia y LatAm 🇨🇴",
    "Caso Práctico": "¡Reto Interactivo! Ponte en los zapatos de un agricultor 🤠",
    
    # Slide 5: History text simplification
    "Registro de hormigas tejedoras en cítricos (China, Dinastía Jin)": "Primeros agricultores usando hormigas para cuidar naranjos en China",
    "Importación de <em>Rodolia cardinalis</em> contra la cochinilla en California": "Importación de la mariquita Rodolia para salvar los cultivos de limón en California (1888)",
    "Concepto del Manejo Integrado de Plagas (MIP) por Stern et al.": "Nacimiento del Manejo Integrado (MIP): combinar métodos para no dañar el planeta",
    "Gurr & Wratten, 2000": "Estudios científicos modernos",

    # Slide 6: Fundamentals
    "Dinámica poblacional y redes tróficas": "Cadenas alimenticias y equilibrio natural",
    "Regulación recíproca entre presas y depredadores": "El juego del gato y el ratón: si hay muchas plagas, crecen los depredadores, y al comerlas todo se equilibra",
    "competencia, parasitismo, depredación": "competencia por espacio, parasitismo (huéspedes) y depredación (cazadores)",

    # Slide 7: Types descriptions
    "Introducción de un enemigo natural exótico para control permanente": "Traer un insecto bueno de otro país para quedarse a vivir y combatir una plaga invasora",
    "Liberación masiva de agentes criados en laboratorio para control rápido": "Criar miles de insectos buenos en laboratorios y liberarlos al campo para frenar una plaga rápido",
    "Modificación del entorno para favorecer poblaciones de enemigos nativos": "Sembrar plantas con flores y evitar venenos para cuidar a los insectos buenos locales",

    # Slide 8: Ladybugs, Lacewings & Wasps
    "Coccinellidae": "Mariquitas (Cazadoras de pulgones)",
    "Chrysopidae": "Crisopas (Los leones de los pulgones)",
    "Hymenoptera": "Avispas Parasitoides (Intrusas que controlan desde adentro)",
    "Son voraces depredadores tanto en su etapa larvaria como adulta. Se alimentan principalmente de pulgones, ácaros y cochinillas, pudiendo consumir hasta 5,000 insectos en su vida.":
        "Son excelentes cazadoras desde que son bebés (larvas) hasta adultas. Comen pulgones y ácaros como si fueran hamburguesas: ¡una sola mariquita puede comer hasta 5,000 plagas en su vida!",
    "Conocidas como \"leones de pulgones\", sus larvas son extremadamente agresivas contra una amplia gama de plagas de cuerpo blando, lo que las convierte en agentes de control versátiles.":
        "Sus larvas son apodadas \"leones de pulgones\" porque tienen mandíbulas enormes y devoran plagas de cuerpo blando sin parar. Son súper útiles en muchos cultivos.",
    "A diferencia de los depredadores, estas avispas ponen sus huevos dentro del huésped. Las larvas se desarrollan internamente, matando a la plaga desde adentro con una precisión letal.":
        "Estas avispitas no pican a los humanos. Ponen sus huevos dentro de los huevos o cuerpos de las plagas. Cuando nacen sus bebés, se alimentan de la plaga por dentro y la eliminan con precisión de superhéroe.",

    # Slide 10: Fungi
    "Infección por esporas de hongos entomopatógenos como <em>Beauveria bassiana</em>": "Cómo el hongo Beauveria enferma y elimina a los insectos malos",
    "Contacto, germinación, penetración cuticular, colonización y esporulación": "Paso a paso: el hongo toca al insecto, entra por su piel, crece por dentro y lo momifica con un polvo blanco",
    
    # Slide 12: MIP
    "Umbral económico de daño": "Límite de daño aceptable",
    "Densidad donde el costo del control iguala las pérdidas potenciales (Stern et al., 1959).": "Punto donde hay tantas plagas que si no actuamos perderemos dinero, pero vigilando antes de que ocurra.",
    "Monitoreo de poblaciones": "Vigilancia constante",
    "Trampas, muestreos visuales y conteos para determinar densidad poblacional y presencia de enemigos naturales.": "Colocar trampas y revisar las hojas para contar cuántos insectos buenos y malos hay antes de tomar decisiones.",
    "Selección de estrategia MIP": "Elegir la mejor defensa",
    "Combinar control biológico, cultural, etológico y químico selectivo según el caso.": "Usar métodos biológicos, trampas de olor, abonos naturales y solo usar químicos si es una emergencia real.",
    "Plaguicidas selectivos": "Insecticidas amigables",
    "Usar solo cuando sea necesario, priorizando productos de bajo impacto sobre enemigos naturales.": "Si hay que usar químicos, elegir los que solo afecten a la plaga y dejen sanos a los insectos buenos.",

    # Slide 13: Advantages / Limits
    "Alta selectividad (específico de la plaga)": "Superespecífico: solo ataca a la plaga sin dañar abejas u otros animales buenos",
    "Baja probabilidad de resistencia": "No genera resistencia: los insectos plaga no se vuelven inmunes tan fácil",
    "Acción más lenta comparada con químicos": "Es más lento: no es inmediato como echar un veneno, requiere paciencia",
    "Dependencia de condiciones climáticas": "Sensible al clima: si hace demasiado frío o calor, los insectos buenos no trabajan igual",
    
    # Slide 14: Risks
    "Desplazamiento de especies nativas": "Invasión de territorio: si traemos insectos de otros países, podrían competir con los locales",
    "Riesgos de saltos de hospedador": "Cambio de menú: peligro de que el insecto traído empiece a comer plantas u otros insectos útiles",
    
    # Slide 15: Futures
    "Liberación automatizada de parasitoides mediante vehículos aéreos no tripulados": "Liberar insectos buenos usando drones equipados con GPS",
    "Detección y monitoreo automatizado con visión artificial y machine learning": "Cámaras inteligentes con IA que detectan plagas y avisan al agricultor en tiempo real"
}

# The user explicitly said: "No trabajes con emojis". So we must remove any emojis from the keys/values.
cleaned_replacements = {}
for k, v in text_replacements.items():
    # Remove emoji characters from keys and values
    k_clean = re.sub(r"[\U00010000-\U0010ffff\u2600-\u27BF️]", "", k).strip()
    v_clean = re.sub(r"[\U00010000-\U0010ffff\u2600-\u27BF️]", "", v).strip()
    cleaned_replacements[k_clean] = v_clean

for src, dest in cleaned_replacements.items():
    html = html.replace(src, dest)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Simplification complete!")
