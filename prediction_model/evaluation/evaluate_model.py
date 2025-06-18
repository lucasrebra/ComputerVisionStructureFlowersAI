import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from prediction_model.models.model_definitions import SimpleCNN
from prediction_model.config.config import TRAINING_CONFIG, EVALUATION_CONFIG

def load_model(model_path):
    model = SimpleCNN()
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model

def evaluate_model(model, test_data_path):
    transform = transforms.Compose([
        transforms.Resize((TRAINING_CONFIG["img_height"], TRAINING_CONFIG["img_width"])),
        transforms.ToTensor(),
    ])

    test_dataset = datasets.ImageFolder(root=test_data_path, transform=transform)
    test_loader = DataLoader(test_dataset, batch_size=TRAINING_CONFIG["batch_size"], shuffle=False)

    correct = 0
    total = 0
    with torch.no_grad():
        for data in test_loader:
            images, labels = data
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f'Accuracy of the network on the test images: {100 * correct / total}%')

if __name__ == "__main__":
    model = load_model(TRAINING_CONFIG["model_save_path"])
    evaluate_model(model, EVALUATION_CONFIG["test_data_path"])

