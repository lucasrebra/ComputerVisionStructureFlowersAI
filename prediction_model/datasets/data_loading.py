from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from prediction_model.config.config import DATA_LOADING_CONFIG
import os

def authenticate_google_drive():
    gauth = GoogleAuth()
    # Carga o crea credenciales
    gauth.LoadCredentialsFile(DATA_LOADING_CONFIG["credentials_file"])
    if gauth.credentials is None:
        # Autenticación en el navegador
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresca las credenciales automáticamente
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile(DATA_LOADING_CONFIG["credentials_file"])
    return GoogleDrive(gauth)

def download_files_from_folder(folder_id, destination_folder):
    drive = authenticate_google_drive()
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder, exist_ok=True)
    file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
    for file in file_list:
        print(f"Descargando {file['title']} a {destination_folder}...")
        file.GetContentFile(os.path.join(destination_folder, file['title']))

if __name__ == "__main__":
    download_files_from_folder(DATA_LOADING_CONFIG["folder_id"], DATA_LOADING_CONFIG["destination_folder"])
