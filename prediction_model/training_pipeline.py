from prediction_model.datasets.data_loading import download_files_from_folder
from prediction_model.datasets.data_cleaning import clean_dataset
from prediction_model.models.train import train_model
from prediction_model.evaluation.evaluate_model import evaluate_model, load_model
from prediction_model.config.config import DATA_LOADING_CONFIG, DATA_CLEANING_CONFIG, TRAINING_CONFIG, EVALUATION_CONFIG

def run_training_pipeline():
    # Paso 1: Cargar los datos (Opcional, dependiendo de si tus datos ya están localmente disponibles)
    print("Iniciando la descarga de datos...")
    download_files_from_folder(DATA_LOADING_CONFIG["folder_id"], DATA_LOADING_CONFIG["destination_folder"])

    # Paso 2: Limpiar y preparar los datos
    print("Limpiando y preparando los datos...")
    clean_dataset()

    # Paso 3: Entrenar el modelo
    print("Iniciando el entrenamiento del modelo...")
    train_model()

    # Paso 4: Evaluar el modelo con los datos de prueba
    print("Evaluando el modelo...")
    model = load_model(TRAINING_CONFIG["model_save_path"])
    evaluate_model(model, EVALUATION_CONFIG["test_data_path"])

if __name__ == "__main__":
    run_training_pipeline()
