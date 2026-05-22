from __future__ import annotations

import argparse


def _preview_batch(batch):
    try:
        import matplotlib.pyplot as plt
        from torchvision.utils import make_grid
    except ImportError as exc:  # pragma: no cover - depends on optional deps
        raise RuntimeError(
            "Previewing batches requires matplotlib and torchvision."
        ) from exc

    images, _labels = batch
    grid = make_grid(images, nrow=8)
    plt.figure(figsize=(14, 8))
    plt.imshow(grid.permute(1, 2, 0))
    plt.title("Dataset preview")
    plt.axis("off")
    plt.show()


def main(argv=None):
    parser = argparse.ArgumentParser(prog="curaset")
    subparsers = parser.add_subparsers(dest="command")

    preview = subparsers.add_parser("preview", help="Preview a dataset batch")
    preview.add_argument("--dataset", required=True, help="Dataset name or path")
    preview.add_argument("--batch-size", type=int, default=32)
    preview.add_argument("--train", action="store_true", help="Use the training split")
    preview.add_argument("--download", dest="download", action="store_true", help="Download built-in datasets")
    preview.add_argument("--no-download", dest="download", action="store_false", help="Do not download built-in datasets")
    preview.set_defaults(download=True)

    args = parser.parse_args(argv)

    if args.command != "preview":
        parser.print_help()
        return 1

    try:
        from curaset.dataset.registry import get_dataset
    except ImportError:  # pragma: no cover - depends on optional deps
        print("CuraSet preview requires the dataset dependencies to be installed.")
        return 2

    data = get_dataset(
        args.dataset,
        batch_size=args.batch_size,
        train=args.train,
        download=args.download,
    )
    print(f"Loaded dataset: {args.dataset}")

    batch = next(iter(data))
    _preview_batch(batch)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
