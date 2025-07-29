from torchvision.datasets import CIFAR10
from torchvision import transforms

def load(train=True, download=True, **kwargs):
    transform = transforms.ToTensor()
    return CIFAR10(root='./data', train=train, transform=transform, download=download)
