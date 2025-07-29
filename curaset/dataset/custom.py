import os
import pandas as pd
from torchvision import datasets, transforms
from torch.utils.data import Dataset, DataLoader
from PIL import Image

class CSVDataset(Dataset):
    def __init__(self, csv_path, transform=None):
        self.data = pd.read_csv(csv_path)
        assert 'image' in self.data.columns and 'label' in self.data.columns, \
            "CSV must contain 'image' and 'label' columns"
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        image_path = self.data.iloc[idx]['image']
        label = self.data.iloc[idx]['label']
        image = Image.open(image_path).convert('RGB')
        if self.transform:
            image = self.transform(image)
        return image, label

def load(path, batch_size=32, shuffle=True, transform=None, num_workers=2, **kwargs):
    if transform is None:
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
        ])

    if os.path.isdir(path):
        dataset = datasets.ImageFolder(path, transform=transform)
    elif os.path.isfile(path) and path.endswith('.csv'):
        dataset = CSVDataset(path, transform=transform)
    else:
        raise ValueError(f"Unsupported dataset path: {path}")

    loader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers)
    return loader
