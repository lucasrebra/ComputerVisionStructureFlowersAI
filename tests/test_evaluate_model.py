import os
import unittest
from unittest.mock import MagicMock, patch
from prediction_model.tests.test_data_loader import TestDataLoader
from prediction_model.test_evaluate_model import evaluate_model

class TestEvaluateModel(unittest.TestCase):
    @patch('prediction_model.test_evaluate_model.load_model')
    def test_evaluate_model_accuracy(self, mock_load_model):
        # Mock de carga del modelo
        mock_model = MagicMock()
        mock_load_model.return_value = mock_model

        # Definir variables de prueba
        test_data_path = 'test_data_path'

        # Mock del dataloader
        mock_data_loader = MagicMock()
        mock_data_loader.__iter__.return_value = iter(TestDataLoader())

        # Mock de torch.utils.data.DataLoader
        with patch('torch.utils.data.DataLoader', return_value=mock_data_loader):
            # Ejecutar la función bajo prueba
            evaluate_model(mock_model, test_data_path)

            # Verificar que se llamó al DataLoader con la ruta de datos de prueba
            torch.utils.data.DataLoader.assert_called_once_with(
                TestDataLoader(), batch_size=TRAINING_CONFIG["batch_size"], shuffle=False)

            # Verificar que se evaluó la precisión del modelo
            mock_model.assert_called_once_with(TRAINING_CONFIG["model_save_path"])
            mock_model.assert_any_call(TestDataLoader()[0][0])  # Primera imagen de los datos de prueba

if __name__ == "__main__":
    unittest.main()
