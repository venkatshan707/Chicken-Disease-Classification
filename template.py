import os
from pathlib import Path
import logging # 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",   
    """ __init__.py  a special Python file that is used to indicate that the directory
      it is present in is a Python package. t can contain initialization code for the package, or it can be an empty file.
   """
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    

]


for filepath in list_of_files:   # for all the files 
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="": 
        """code checks if the variable filedir have some file directory value. 
        If its not empty, it creates the specified directory using os.makedirs on file explorer and logs an informational
         message using logging.info
        """
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        """ if the file specified by filepath does not exist or has a size of 0 bytes, 
        it creates an empty file and logs a message indicating the creation of the empty file.
        """
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")
        #if file already created just skip 