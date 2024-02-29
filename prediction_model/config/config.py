import os

# Directorio base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Configuraciones para la carga de datos desde Google Drive
DATA_LOADING_CONFIG = {
    "folder_id": "your_google_drive_folder_id_here",
    "destination_folder": os.path.join(BASE_DIR, "datasets", "raw"),
    "credentials_file": os.path.join(BASE_DIR, "credentials", "mycreds.txt"),
}

# Configuraciones para la limpieza de datos
DATA_CLEANING_CONFIG = {
    "dataset_path": os.path.join(BASE_DIR, "datasets", "raw"),
    "output_folder_path": os.path.join(BASE_DIR, "datasets", "processed"),
    "embeddings_csv": os.path.join(BASE_DIR, "datasets", "embeddings.csv"),
    "filtered_embeddings_csv": os.path.join(BASE_DIR, "datasets", "filtered_embeddings.csv"),
}

# Configuraciones para el entrenamiento del modelo
TRAINING_CONFIG = {
    "batch_size": 32,
    "img_height": 180,
    "img_width": 180,
    "epochs": 50,
    "validation_split": 0.2,
    "seed": 123,
    "early_stopping_patience": 10,
    "model_save_path": os.path.join(BASE_DIR, "trained_models", "flowers_classification.h5"),
}

# Configuraciones para el modelo preentrenado ResNet50
RESNET50_CONFIG = {
    "pretrained": True,
    "include_top": False,
    "weights": "imagenet",
    "input_shape": (224, 224, 3),
}

# Configuración para Transfer Learning
TRANSFER_LEARNING_CONFIG = {
    "base_model_weights": "imagenet",
    "include_top": False,
    "pooling": "avg",
    "trainable_layers": 2,
}

# Otras configuraciones globales
GLOBAL_CONFIG = {
    "random_state": 42,
}

