from . import cifar, mnist, custom

DATASET_REGISTRY = {
    "cifar": cifar.load,
    "mnist": mnist.load,
    "custom": custom.load,
}

def get_dataset(name_or_path, **kwargs):
    if name_or_path in DATASET_REGISTRY:
        return DATASET_REGISTRY[name_or_path](**kwargs)
    else:
        return custom.load(path=name_or_path, **kwargs)
