"""
Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). 
Copy these files from their current location to a new folder.
"""
#! python3

from pathlib import Path
import sys
import os 
import shutil


EXTENSIONS = {
    ".txt": "text_files",
    ".jpg": "image_files",
    ".jpeg": "image_files",
    ".png": "image_files",
    ".pdf": "pdf_files",
    ".csv": "data_files",
    ".json": "data_files",
    ".py": "python_files",
    ".xlsx": "excel_files",
    ".docx": "word_files",
    # Ajoute d'autres extensions ici si besoin
}



def get_path(path) : 
    path = Path(path) #Make sure the path is not a string but a Path object

    if not path.exists() : 
        print("The path does not exist")
        sys.exit()

    elem = [e for e in path.iterdir() if e.is_file()]
    return elem 
 


def get_extention(file : Path) : 
    return file.suffix.lower()
        

def create_folders(base_path : Path, ext : str) :
    folder_name = EXTENSIONS.get(ext, "autre_fichier")
    target_folder : Path = base_path/folder_name

    target_folder.mkdir(exist_ok=True)
    return target_folder
    
    

def move_files(file_path : Path, target_folder: Path) :
    destination_folder : Path = target_folder/file_path.name
    shutil.move(str(file_path), str(destination_folder))
    print(f"Déplacé : {file_path.name} → {target_folder.name}/")    


def clean_empty_folder(path : Path) : 
    for folder in Path(path).iterdir():
        if folder.is_dir() and not any(folder.iterdir()):
            folder.rmdir()
            print(f"Supprimé dossier vide : {folder.name}")


def main() : 
    if len(sys.argv) < 2 : 
        print("Usage : python file_organisation.py [folder_name]")
        sys.exit()

    path = sys.argv[1]

    path = Path(path)

    file_path = get_path(path)

    try : 

        for file in file_path : 
            ext = get_extention(file)
            target_folder = create_folders(path,ext)
            move_files(file, target_folder)
        
        clean_empty_folder(path)

    except Exception as e : 
        print(f"Error : {e}")
        
    
main()