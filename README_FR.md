# [:es:](README_ES.md) [:de:](README_DE.md) [:uk:](README.md)
### Plugin GIMP 3.0 : Exporter en WebP Optimisé

Il s'agit d'un plugin Python pour GIMP 3.0 conçu pour optimiser et exporter des images spécifiquement pour le web. Il convertit automatiquement votre image au format WebP en garantissant une compression efficace et une taille de fichier minimale (objectif < 2 Mo), idéal pour les projets web modernes.

**Fonctionnalités principales :**
* **Aplatissement de l'image :** Fusionne tous les calques en un seul avant l'exportation.
* **Redimensionnement intelligent :** Si la hauteur de l'image dépasse 1080px, elle est automatiquement réduite à 1080px tout en conservant les proportions.
* **Ajustement de la résolution :** Règle la résolution à 72 DPI, le standard pour les écrans.
* **Exportation WebP :** Sauvegarde l'image avec une qualité de 80 % et une compression avec perte pour un équilibre parfait entre taille et rendu visuel.
* **Nettoyage des métadonnées :** Supprime les données inutiles pour le web (EXIF, IPTC, XMP, profils colorimétriques et miniatures) afin de réduire la taille au maximum.
* **Sauvegarde automatique :** Exporte le fichier dans le même dossier que l'image d'origine, ou sur le Bureau s'il s'agit d'un nouveau fichier.

**Installation :**
1. Enregistrez le code dans un fichier `.py` (par exemple : `export_web.py`).
2. Déplacez le fichier dans le dossier des plugins de GIMP 3.0 (`Édition > Préférences > Dossiers > Plug-Ins`).
3. Assurez-vous de donner les droits d'exécution au fichier (sous Unix : `chmod +x export_web.py`).
4. Redémarrez GIMP.

**Utilisation :**
Ouvrez une image dans GIMP 3.0 et naviguez dans le menu supérieur vers :
`Image > File > Export > Export to webp`

**Crédits :**
Développé par Maya López & Sergio (2026).