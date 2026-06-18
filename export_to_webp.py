#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import gi
gi.require_version('Gimp', '3.0')
from gi.repository import Gimp
gi.require_version('GimpUi', '3.0')
from gi.repository import GimpUi
from gi.repository import GLib
from gi.repository import Gio
import os 

class ExportWeb (Gimp.PlugIn):
    def do_query_procedures(self):
        return [ "plugin-export-to-webp" ]

    def do_set_i18n (self, name):
        return False

    def do_create_procedure(self, name):
        procedure = Gimp.ImageProcedure.new(self, name,
                                            Gimp.PDBProcType.PLUGIN,
                                            self.run, None)
        procedure.set_image_types("*")
        procedure.set_menu_label("Export to webp")
        procedure.add_menu_path('<Image>/File/Export')

        procedure.set_documentation("Exports file optimized for web (< 2MB target) in WebP format",
                                    "Plugin export to web",
                                    name)
        procedure.set_attribution("Maya López & Sergio", "Sergio", "2026")
        return procedure

    def run(self, procedure, run_mode, image, drawables, config, run_data):
        # 1. Flatten Image (Acoplar capas)
        flatten_proc = Gimp.get_pdb().lookup_procedure('gimp-image-flatten')
        flatten_conf = flatten_proc.create_config()
        flatten_conf.set_property('image', image)
        flatten_proc.run(flatten_conf)
        
        width = image.get_width()
        height = image.get_height()

        # 2. Scale if too large (Escalar si es muy alta)
        if height > 1080:
            new_height = 1080
            new_width = int((width * new_height) / height)

            scale_proc = Gimp.get_pdb().lookup_procedure('gimp-image-scale')
            scale_conf = scale_proc.create_config()
            scale_conf.set_property('image', image)
            scale_conf.set_property('new-width', new_width)
            scale_conf.set_property('new-height', new_height)
            scale_proc.run(scale_conf)

        # 3. Set Resolution (Fijar a 72 DPI)
        res_proc = Gimp.get_pdb().lookup_procedure('gimp-image-set-resolution')
        res_conf = res_proc.create_config()
        res_conf.set_property('image', image)
        res_conf.set_property('xresolution', 72.0)
        res_conf.set_property('yresolution', 72.0)
        res_proc.run(res_conf)

        # 4. Determinar la ruta de guardado de forma segura
        gfile = image.get_file()
        
        if gfile:
            complete_path = gfile.get_path()
            basedir = os.path.dirname(complete_path)
            name_with_extension = os.path.basename(complete_path)
            name_without_extension = os.path.splitext(name_with_extension)[0]
        else:
            basedir = GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DESKTOP)
            if not basedir:
                basedir = os.path.expanduser("~")
            name_without_extension = "web_export"

        # 5. Definir el nombre final con extensión .webp obligatoria
        new_filename = os.path.join(basedir, name_without_extension + ".webp")
        
        # 6. Crear el objeto Gio.File requerido
        save_file = Gio.File.new_for_path(new_filename)

        # 7. WebP Export (Adaptado estrictamente a la firma exacta de tu PDB)
        export_proc = Gimp.get_pdb().lookup_procedure('file-webp-export')
        save_conf = export_proc.create_config()
        
        # Parámetros básicos obligatorios
        save_conf.set_property('run-mode', Gimp.RunMode.NONINTERACTIVE)
        save_conf.set_property('image', image)
        save_conf.set_property('file', save_file)
        
        # Objeto de opciones requerido por la firma (inicializado por defecto)
        save_conf.set_property('options', None) 
        
        # Configuración de compresión y calidad
        save_conf.set_property('preset', 0)                  # 0 = Default
        save_conf.set_property('lossless', False)             # Activamos compresión con pérdidas
        save_conf.set_property('quality', 80)                 # Calidad al 80%
        save_conf.set_property('alpha-quality', 80)           # Calidad de transparencia
        save_conf.set_property('use-sharp-yuv', False)
        
        # Parámetros obligatorios de animación (aunque esté desactivada)
        save_conf.set_property('animation', False)
        save_conf.set_property('animation-loop', False)
        save_conf.set_property('keyframe-distance', 50)       # Requerido por la firma
        save_conf.set_property('default-delay', 100)          # Requerido por la firma
        save_conf.set_property('force-delay', False)          # Requerido por la firma
        
        # Optimización extrema de tamaño
        save_conf.set_property('minimize-size', True)
        
        # Limpieza de metadatos pesados para optimizar la carga en Vercel
        save_conf.set_property('include-exif', False)
        save_conf.set_property('include-iptc', False)
        save_conf.set_property('include-xmp', False)
        save_conf.set_property('include-color-profile', False)
        save_conf.set_property('include-thumbnail', False)
        
        # Ejecutamos el procedimiento
        result = export_proc.run(save_conf)

        return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())

Gimp.main(ExportWeb.__gtype__, sys.argv)