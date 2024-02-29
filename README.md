# Prediction Model Package

## Descripción

Este paquete permite la limpieza, entrenamiento y evaluación de modelos de clasificación de imágenes, especializado en la detección de flores. Fue diseñado para facilitar el proceso desde la carga de los datos hasta la obtención de un modelo entrenado y evaluado.

## Instalación

Para instalar el paquete, sigue estos pasos:

```bash
git clone https://tu-repositorio.git
cd prediction_model
pip install .
```

## Uso

El paquete se puede utilizar de la siguiente manera para entrenar un modelo con tus datos de imágenes. Asegúrate de tener tus datos organizados y configurar correctamente los parámetros en `config.py`.

```python
from prediction_model.training_pipeline import run_training_pipeline

# Ejecuta el pipeline completo de entrenamiento
run_training_pipeline()
```

## Contribuciones

Las contribuciones son bienvenidas y apreciadas. Si tienes sugerencias para mejorar este paquete o has encontrado un error, por favor, considera lo siguiente:

- Abre un issue para discutir los cambios propuestos o reportar un error.
- Para cambios directos, por favor, haz un fork del repositorio, haz tus cambios y envía un pull request para su revisión.

Antes de enviar un pull request, asegúrate de que tu código sigue las convenciones establecidas en el proyecto y pasa todas las pruebas existentes. Además, considera añadir pruebas para nuevas funcionalidades o correcciones.


## Contacto

Para preguntas o consultas adicionales sobre este proyecto, por favor, no dudes en contactarme:

- **Nombre**: Lucas Rey Braga
- **Correo electrónico**: lucasrebra
- **GitHub**: [lucasrebra](https://github.com/lucasrebra)

Agradecemos tu interés en este proyecto y esperamos tus contribuciones y feedback.
