import matplotlib.pyplot as plt
import torchvision.utils
import argparse
from curaset.dataset.registry import get_dataset


def main(data):
    for images, labels in data:
        grid = torchvision.utils.make_grid(images, nrow=8)
        plt.figure(figsize=(15, 8))
        plt.imshow(grid.permute(1, 2, 0))  # Convert CHW to HWC
        plt.title("Sample Image Batch")
        plt.axis('off')
        plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, required=True)
    args = parser.parse_args()

    data = get_dataset(args.dataset)
    print(f"Loaded dataset: {args.dataset}")
    main(data)