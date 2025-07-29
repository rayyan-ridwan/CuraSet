# 🧹 CuraSet

![logo](https://github.com/user-attachments/assets/169ee8cd-3384-43cc-9fe8-4504338483e4)

> **Clean data. Trust results.**  
> CuraSet helps you detect label noise, quantify uncertainty, and improve dataset hygiene — because better data means better models.


---

## ✨ Overview

Machine learning models are only as good as the data they train on.  
**CuraSet** is an open-source tool for **data-centric AI**, focused on:

- 🔍 Identifying **label noise** in datasets
- 📉 Estimating **sample-level uncertainty**
- 📊 Visualizing and exporting **data quality reports**
- ⚙️ Integrating seamlessly with your existing PyTorch or scikit-learn workflows

Use CuraSet as a **CLI tool**, **Python library**, or integrate it into your **training pipeline**.

---

## 🔧 Features

| Feature | Description |
|--------|-------------|
| 🧪 Label Noise Detection | Detect mislabeled examples using confident learning, disagreement, or uncertainty |
| 🎯 Uncertainty Scoring | Entropy, margin sampling, variance over ensemble predictions |
| 📊 Hygiene Reports | Visual and tabular reports of dataset quality |
| 🛠 CLI + API | Run from terminal or import into your pipeline |
| 💾 Export Options | Export clean splits, noise masks, or quality scores to CSV |

---

## Installation

```bash
pip install curaset
````

Or install from source:

```bash
git clone https://github.com/rayyan-ridwan/CuraSet.git
cd CuraSet
pip install -e .
```

---

## Usage

### 🛠 Option 1: CLI (Command Line)

```bash
curaset detect-noise \
    --dataset cifar10 \
    --method disagreement \
    --threshold 0.2 \
    --output noise_mask.csv
```

Or run uncertainty scoring:

```bash
curaset score-uncertainty \
    --logits logits.npy \
    --metric entropy \
    --output entropy_scores.csv
```

### 🧑‍💻 Option 2: Python API

```python
from curaset.noise_detect import disagreement_score
from curaset.uncertainty import entropy

# Logits from ensemble or saved model
logits = np.load("logits.npy")
probs = softmax(logits, axis=1)

# Calculate entropy
unc_scores = entropy(probs)

# Detect noise
preds = np.argmax(probs, axis=1)
ensemble_preds = np.stack([preds, preds, preds])  # Simulate ensemble
noise_scores = disagreement_score(ensemble_preds.T)
```

---

## 📊 Output Files

| File                     | Description                            |
| ------------------------ | -------------------------------------- |
| `noise_mask.csv`         | Binary mask (1 = noisy)                |
| `uncertainty_scores.csv` | Sample-wise uncertainty values         |
| `clean_data.csv`         | Export of filtered/clean dataset       |
| `report.md`              | Summary of noise and uncertainty stats |

---

## 🧪 Example: Run on CIFAR-10

```bash
curaset detect-noise \
    --dataset cifar10 \
    --method entropy \
    --threshold 0.15
```

Or try with your own model logits:

```bash
curaset score-uncertainty \
    --logits saved_logits.npy \
    --metric margin
```

Or you can generate a noise report:
```bash
curaset report \
    --noise noise_mask.csv \
    --uncertainty entropy_scores.csv \
    --output report.md
```

---

## 📈 Planned Features (Want to help?)
* [ ] Implementation and design functionality
* [ ] Bootstrap-based confidence intervals for noise/uncertainty
* [ ] GUI dashboard (maybe Streamlit)
* [ ] Support for HuggingFace datasets
* [ ] Visualizer for noisy samples
* [ ] Integration with `cleanlab`, `wandb`, `label-studio`

---

## 🤝 Contributing

CuraSet is open to all contributors, researchers, students, developers.
Read [`CONTRIBUTING.md`](./CONTRIBUTING.md) to get started.

---

## 📄 License

MIT License | free for academic, commercial, and personal use.

---

## 👨‍🔬 Maintainer

Built and maintained by [Rayyan Ridwan](https://github.com/rayyan-ridwan), with ❤️ for data quality and open science.

---

## 🌍 Join the Community

Open a [GitHub Discussion](https://github.com/CuraSet/discussions) to share ideas, questions, or feedback.

---
