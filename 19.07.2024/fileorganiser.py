import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):
            file_ext = filename.split('.')[-1].lower()
            if file_ext == filename:
                continue
            
            ext_dir = os.path.join(directory, file_ext)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            
            shutil.move(file_path, os.path.join(ext_dir, filename))
            print(f"Moved: {filename} -> {ext_dir}")

directory = 'files_to_organize'
organize_files(directory)
