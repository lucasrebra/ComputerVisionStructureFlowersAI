import os
import unittest
from unittest.mock import MagicMock, patch
from prediction_model.datasets.data_loading import download_files_from_folder

class TestDataLoading(unittest.TestCase):
    @patch('prediction_model.datasets.data_loading.authenticate_google_drive')
    def test_download_files_from_folder(self, mock_authenticate_google_drive):
        # Mock de la autenticación de Google Drive
        mock_drive = MagicMock()
        mock_authenticate_google_drive.return_value = mock_drive

        # Definir variables de prueba
        folder_id = 'test_folder_id'
        destination_folder = 'test_destination_folder'
        # Crear mocks de archivos devueltos por PyDrive
        file_list = []
        for title in ['file1.txt', 'file2.txt']:
            file_mock = MagicMock()
            file_mock.__getitem__.side_effect = lambda key, t=title: t if key == 'title' else None
            file_list.append(file_mock)

        # Mock del listado de archivos en la carpeta
        mock_drive.ListFile.return_value.GetList.return_value = file_list

        # Ejecutar la función bajo prueba
        download_files_from_folder(folder_id, destination_folder)

        # Verificar que se llamó al método ListFile con el ID de la carpeta
        mock_drive.ListFile.assert_called_once_with({'q': f"'{folder_id}' in parents and trashed=false"})

        # Verificar que se descargaron los archivos en la carpeta de destino
        for file_mock in file_list:
            file_mock.GetContentFile.assert_any_call(
                os.path.join(destination_folder, file_mock['title']))

if __name__ == "__main__":
    unittest.main()
