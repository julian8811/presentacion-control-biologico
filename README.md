# Presentación: Control Biológico

Presentación web interactiva sobre control biológico en agricultura sostenible.

**Sitio en vivo:** [diaposcontrol.vercel.app](https://diaposcontrol.vercel.app/)

## Estructura del repositorio

```
├── index.html              # Presentación (archivo desplegado por Vercel)
├── assets/
│   ├── images/             # Ilustraciones en WebP
│   └── videos/             # Videos MP4 optimizados
├── docs/                   # Material de apoyo (investigación, cuestionario)
└── scripts/                # Herramientas de mantenimiento
```

## Desarrollo local

Abre `index.html` con un servidor estático:

```bash
npx serve .
```

O con Python:

```bash
python -m http.server 8080
```

## Optimización de medios

Requiere Node.js 20+ y dependencias de desarrollo (`npm install`).

```bash
npm install
node scripts/optimize-images.mjs   # JPEG/PNG → WebP
node scripts/optimize-videos.mjs   # Recomprime MP4
node scripts/optimize-html.mjs     # Carga diferida por diapositiva
node scripts/verify.mjs            # Verifica referencias
```

## Despliegue

El proyecto se despliega automáticamente en Vercel al hacer push a `main`. Solo `index.html` en la raíz y la carpeta `assets/` son necesarios para producción.
