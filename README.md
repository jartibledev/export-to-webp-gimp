# [:es:](README.md) [:de:](README_DE.md) [:fr:](README_FR.md) 
### GIMP 3.0 Plugin: Optimized WebP Export

This is a Python-based plugin for GIMP 3.0 designed to optimize and export images specifically for web use. It automatically converts your canvas to the WebP format, ensuring efficient compression and minimal file size (target < 2MB), making it ideal for modern web projects.

**Main Features:**
* **Image Flattening:** Merges all layers into a single layer before exporting.
* **Smart Scaling:** If the image height exceeds 1080px, it automatically scales it down to 1080px while maintaining the original aspect ratio.
* **Resolution Adjustment:** Sets the image resolution to 72 DPI, the standard for screens.
* **WebP Export:** Saves the image at 80% quality with lossy compression to achieve the perfect balance between file size and visual quality.
* **Metadata Stripping:** Removes heavy, unnecessary data for the web (EXIF, IPTC, XMP, color profiles, and thumbnails) to maximize size reduction.
* **Automatic Saving:** Exports the file to the same directory as the original image, or to the Desktop if the file is new/unsaved.

**Installation:**
1. Save the code into a `.py` file (e.g., `export_web.py`).
2. Move the file to your GIMP 3.0 plugins folder (`Edit > Preferences > Folders > Plug-Ins`).
3. Make sure to grant execution permissions to the file (on Unix-based systems: `chmod +x export_web.py`).
4. Restart GIMP.

**Usage:**
Open any image in GIMP 3.0 and navigate the top menu to:
`Image > File > Export > Export to webp`

**Credits:**
Developed by Maya López & Sergio (2026).

