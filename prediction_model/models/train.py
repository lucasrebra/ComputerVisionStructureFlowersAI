import torch
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from prediction_model.models.model_definitions import SimpleCNN
from prediction_model.config.config import TRAINING_CONFIG

def train_model():
    transform = transforms.Compose([
        transforms.Resize((TRAINING_CONFIG["img_height"], TRAINING_CONFIG["img_width"])),
        transforms.ToTensor(),
    ])

    # Asume que tienes un conjunto de datos personalizado compatible con PyTorch
    train_dataset = datasets.ImageFolder(root=TRAINING_CONFIG["dataset_path"], transform=transform)
    train_loader = DataLoader(train_dataset, batch_size=TRAINING_CONFIG["batch_size"], shuffle=True)

    model = SimpleCNN()
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters())

    for epoch in range(TRAINING_CONFIG["epochs"]):
        model.train()
        for batch_idx, (data, target) in enumerate(train_loader):
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
            print(f'Epoch {epoch}, Batch {batch_idx}, Loss {loss.item()}')

    # Guardar el modelo
    torch.save(model.state_dict(), TRAINING_CONFIG["model_save_path"])

if __name__ == "__main__":
    train_model()
