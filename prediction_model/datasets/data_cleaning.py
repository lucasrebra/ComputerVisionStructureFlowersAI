import os
from shutil import copyfile, copytree
from prediction_model.config.config import DATA_CLEANING_CONFIG

def clean_dataset():
    """Simple cleaning step that copies raw data to a processed folder."""
    src = DATA_CLEANING_CONFIG["dataset_path"]
    dst = DATA_CLEANING_CONFIG["output_folder_path"]
    if not os.path.exists(src):
        raise FileNotFoundError(f"Dataset path '{src}' does not exist")
    if os.path.exists(dst):
        # Allow running multiple times by merging contents
        copytree(src, dst, dirs_exist_ok=True)
    else:
        copytree(src, dst)
    print(f"Dataset cleaned and copied to {dst}")

def download_dataset_from_drive(dataset_path, destination_path):
    """
    Copia el dataset desde una ubicación en Google Drive a un directorio local.
    
    :param dataset_path: Ruta al dataset en Google Drive (asumiendo que Drive ya está montado).
    :param destination_path: Ruta local donde se guardará el dataset.
    """
    if not os.path.exists(destination_path):
        os.makedirs(destination_path, exist_ok=True)
    copyfile(dataset_path, destination_path)
    print(f"Dataset copiado a {destination_path}")
