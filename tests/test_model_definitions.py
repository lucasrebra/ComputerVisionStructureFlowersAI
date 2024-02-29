import torch
import unittest
from prediction_model.models.model_definitions import SimpleCNN

class TestSimpleCNN(unittest.TestCase):
    def setUp(self):
        self.model = SimpleCNN()

    def test_forward_pass(self):
        # Crear un tensor de prueba con las dimensiones correctas
        input_tensor = torch.randn(1, 3, 224, 224)  # batch_size=1, canales RGB, imagen de 224x224

        # Ejecutar un pase hacia adelante a través del modelo
        output_tensor = self.model(input_tensor)

        # Verificar que la salida tiene la forma correcta
        self.assertEqual(output_tensor.shape, torch.Size([1, 2]))  # Asumiendo clasificación binaria

if __name__ == "__main__":
    unittest.main()
