from PIL import Image
import torch
from torchvision import transforms
from prediction_model.models.model_definitions import SimpleCNN
from prediction_model.config.config import TRAINING_CONFIG
from evaluation.evaluate_model import load_model

def predict_image(image_path, model):
    transform = transforms.Compose([
        transforms.Resize((TRAINING_CONFIG["img_height"], TRAINING_CONFIG["img_width"])),
        transforms.ToTensor(),
    ])

    image = Image.open(image_path)
    image = transform(image).float()
    image = image.unsqueeze(0)  # Añade una dimensión de batch

    output = model(image)
    _, predicted = torch.max(output.data, 1)
    
    return predicted

if __name__ == "__main__":
    model_path = TRAINING_CONFIG["model_save_path"]
    model = load_model(model_path)  # Asegúrate de definir `load_model` como en `evaluate_model.py`
    image_path = 'path/to/your/test/image.jpg'
    prediction = predict_image(image_path, model)
    print(f'Predicted class: {prediction.item()}')
