import os
from shutil import copyfile

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
