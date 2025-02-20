# here we are creating a template / directory automatically using this template
import os 
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO)

project_name = "ml_project_1"

list_of_files = [

    ".github/workflows/.gitkeep", #this is just an indication that we are creating an github folder which will be used in deployment 
    f"src/{project_name}/__init__.py", # inside src we are creating MLProject init is used to create package
    f"src/{project_name}/components/data_ingestion.py", 
    f"src/{project_name}/components/data_transformation.py", 
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/piplelines/__init__.py", 
    f"src/{project_name}/piplelines/training_pipeline.py",    
    f"src/{project_name}/piplelines/prediction_pipeline.py",    
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "README.md",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath) #path relative directory
    filedir, filename = os.path.split(filepath) # split the path into directory and filename

    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # create the directory if it does not exist
        logging.info(f"Creating directory:{filedir} for the file {filename}")
         
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # check if file does not exist or file is empty
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists") # if file is already exists
        