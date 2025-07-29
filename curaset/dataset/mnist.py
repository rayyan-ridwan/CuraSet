from torchvision.datasets import MNIST
from torchvision import transforms

def load(train=True, download=True, **kwargs):
    transform = transforms.ToTensor()
    return MNIST(root='./data', train=train, transform=transform, download=download)
