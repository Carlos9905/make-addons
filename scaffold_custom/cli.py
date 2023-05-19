import os
import shutil
import sys
from tqdm import tqdm

from scaffold_custom.description import MANIFEST_FILE_BRAINTECH, MANIFEST_FILE_MULTISERVICIOS

def create_project(client:int,tecnical_name:str):
    os.mkdir(tecnical_name)
    folders = ['models', 'views', 'security', 'reports', 'static', 'wizard', 'controllers']
    for folder in tqdm(folders, desc='Creating files'):
        #Crear los archivos de inicio para el módulo nuevo
        open(os.path.join(tecnical_name, "__init__.py"), 'a').close()
        open(os.path.join(tecnical_name, "__manifest__.py"), 'a').close()
        
        #Crea las carpetas principales
        path_folder = os.path.join(tecnical_name, folder)
        os.mkdir(path_folder)
        
        #Crea los archivos de inicio para las carpetas
        if folder in ['models', 'wizard', 'controllers']:
            open(os.path.join(path_folder, '__init__.py'), 'a').close()
        if folder == 'security':
            open(os.path.join(path_folder, 'ir.model.access.csv'), 'w').write('id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink\n')
        if folder == 'static':
            description_folder = os.path.join(path_folder, 'description')
            os.mkdir(description_folder)
            
            #Para Multiserviciosrl
            #Copia el icono del módulo
            if client == '1':
                src_image = os.path.join(os.path.dirname(__file__), 'src', 'img', 'mrl.png')
                dest_image = os.path.join(description_folder, 'icon.png')
                shutil.copy(src_image, dest_image)
            
            #Para BrainTech
            #Copia el icono del módulo
            elif client == '2':
                src_image = os.path.join(os.path.dirname(__file__), 'src', 'img', 'btch.png')
                dest_image = os.path.join(description_folder, 'icon.png')
                shutil.copy(src_image, dest_image)
    
    # Agrega los imports al __init__.py
    with open(os.path.join(tecnical_name, '__init__.py'), 'a') as f:
        f.write('from . import models\nfrom . import controllers\nfrom . import wizard\n')
    
    # Agrega la informacion al __manifest__.py
    if client == '1':
        with open(os.path.join(tecnical_name, '__manifest__.py'), 'a') as f:
            f.write('{\n')
            for key, value in MANIFEST_FILE_MULTISERVICIOS.items():
                f.write(f"    '{key}': {repr(value)},\n")
            f.write('}\n')
    elif client == '2':
        with open(os.path.join(tecnical_name, '__manifest__.py'), 'a') as f:
            f.write('{\n')
            for key, value in MANIFEST_FILE_BRAINTECH.items():
                f.write(f"    '{key}': {repr(value)},\n")
            f.write('}\n')
    
    print(f"Se ha creado el área de trabajo '{tecnical_name}' con éxito.")

def main():
    client = input("Client:\n 1. Multiserviciosrl.\n 2. BrainTech\n 3. Exit\n")
    if client == "3":
        sys.exit()
    name = input("Tencnical name: ")
    create_project(client, name)

if __name__ == "__main__":
    main()