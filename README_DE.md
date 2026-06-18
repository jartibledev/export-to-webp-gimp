# [:es:](README_ES.md) [:fr:](README_FR.md) [:uk:](README.md) 
### GIMP 3.0 Plugin: Für WebP optimiert exportieren

Dies ist ein Python-basiertes Plugin für GIMP 3.0, das speziell für die Optimierung und den Export von Bildern für die Webnutzung entwickelt wurde. Es konvertiert Ihr Bild automatisch in das WebP-Format und sorgt für eine effiziente Komprimierung bei minimaler Dateigröße (Ziel < 2 MB), ideal für moderne Webprojekte.

**Hauptmerkmale:**
* **Bild zusammenfügen:** Reduziert alle Ebenen vor dem Export auf eine einzige Ebene.
* **Intelligente Skalierung:** Wenn die Bildhöhe 1080px überschreitet, wird sie automatisch unter Beibehaltung des Seitenverhältnisses auf 1080px herunterskaliert.
* **Auflösungsanpassung:** Setzt die Auflösung auf 72 DPI, den Standard für Bildschirme.
* **WebP-Export:** Speichert das Bild in 80% Qualität mit verlustbehafteter Komprimierung für das perfekte Gleichgewicht zwischen Dateigröße und visueller Qualität.
* **Metadaten-Bereinigung:** Entfernt schwere, für das Web unnötige Daten (EXIF, IPTC, XMP, Farbprofile und Vorschaubilder), um die Dateigröße drastisch zu reduzieren.
* **Automatisches Speichern:** Exportiert die Datei in dasselbe Verzeichnis wie das Originalbild oder auf den Desktop, falls das Bild noch nicht gespeichert wurde.

**Installation:**
1. Speichern Sie den Code in einer `.py`-Datei (z. B. `export_web.py`).
2. Verschieben Sie die Datei in den GIMP 3.0-Plug-In-Ordner (`Bearbeiten > Einstellungen > Ordner > Plug-Ins`).
3. Stellen Sie sicher, dass die Datei Ausführungsrechte besitzt (unter Unix: `chmod +x export_web.py`).
4. Starten Sie GIMP neu.

**Verwendung:**
Öffnen Sie ein Bild in GIMP 3.0 und navigieren Sie im oberen Menü zu:
`Image > File > Export > Export to webp`

**Credits:**
Entwickelt von Maya López & Sergio (2026).