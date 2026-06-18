# [:uk:](README.md) [:de:](README_DE.md) [:fr:](README_FR.md)
### Plugin GIMP 3.0: Exportar a WebP Optimizado

Este es un plugin basado en Python para GIMP 3.0 diseñado para optimizar y exportar imágenes específicamente para uso web. Convierte automáticamente tu lienzo al formato WebP garantizando una compresión eficiente y un tamaño de archivo mínimo (objetivo < 2MB), ideal para proyectos web modernos como plataformas en Vercel.

**Características principales:**
* **Acoplamiento de capas:** Fusiona todas las capas en una sola antes de exportar.
* **Redimensionamiento inteligente:** Si la imagen tiene una altura superior a 1080px, la escala automáticamente a 1080px manteniendo la proporción original.
* **Ajuste de resolución:** Establece la resolución a 72 DPI, el estándar óptimo para pantallas.
* **Exportación a WebP:** Guarda la imagen en calidad del 80% con compresión con pérdidas para lograr un balance perfecto entre peso y calidad visual.
* **Limpieza de metadatos:** Elimina datos pesados e innecesarios para la web (EXIF, IPTC, XMP, perfiles de color y miniaturas) para exprimir al máximo la reducción de tamaño.
* **Guardado automático:** Exporta el archivo en el mismo directorio que la imagen original, o en el Escritorio si el archivo es nuevo.

**Instalación:**
1. Guarda el código en un archivo con extensión `.py` (ejemplo: `export_web.py`).
2. Mueve el archivo a la carpeta de plugins de GIMP 3.0 (`Edit > Preferences > Folders > Plug-Ins`).
3. Asegúrate de otorgar permisos de ejecución al archivo (en sistemas basados en Unix: `chmod +x export_web.py`).
4. Reinicia GIMP.

**Uso:**
Abre cualquier imagen en GIMP 3.0 y navega por el menú superior hasta:
`Image > File > Export > Export to webp`

**Créditos:**
Desarrollado por Maya López & Sergio (2026).