# CuraSet

<p align="center">
  <strong>Clean data. Better models.</strong>
</p>

CuraSet is a lightweight Python toolkit for dataset inspection, image previewing, and the early building blocks of label-noise and uncertainty workflows.

## What it does

- Load common vision datasets like CIFAR-10 and MNIST
- Preview image batches from folders, CSV manifests, or built-in datasets
- Provide a small, clean package structure for expanding into data-quality tooling

## Installation

```bash
pip install -e .
```

## Quick start

Preview a dataset batch:

```bash
curaset preview --dataset cifar
```

Load a local folder or CSV manifest:

```bash
curaset preview --dataset /path/to/dataset
```

## Package structure

```text
curaset/
├── __init__.py
├── cli.py
├── dataset/
│   ├── __init__.py
│   ├── cifar.py
│   ├── custom.py
│   ├── mnist.py
│   └── registry.py
├── detectors/
├── reports/
└── uncertainty/
```

## Roadmap

- Dataset quality checks
- Sample-level uncertainty scoring
- Noise detection strategies
- Exportable reports and summaries

## Development

```bash
python -m compileall curaset
```

## Contributing

Contributions are welcome. See [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## License

MIT
