import os
import unittest
import torch
from prediction_model.train import train_model
from prediction_model.models.model_definitions import SimpleCNN
from prediction_model.config.config import TRAINING_CONFIG

class TestTrain(unittest.TestCase):
    def setUp(self):
        self.model_save_path = "test_model.pth"  # Ruta para guardar el modelo de prueba

    def test_train_model(self):
        # Verificar que el modelo se entrena sin errores
        train_model()

        # Verificar que se guarda un archivo de modelo
        self.assertTrue(os.path.exists(self.model_save_path))

        # Verificar que el modelo guardado puede ser cargado correctamente
        model = SimpleCNN()
        model.load_state_dict(torch.load(self.model_save_path))
        self.assertIsInstance(model, torch.nn.Module)

    def tearDown(self):
        # Eliminar el archivo de modelo de prueba después de la ejecución del test
        if os.path.exists(self.model_save_path):
            os.remove(self.model_save_path)

if __name__ == "__main__":
    unittest.main()
