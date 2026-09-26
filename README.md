# Evaluating Large Language Models on Discontinuous Arabic Multiword Expressions: A Case Study using PARSEME-AR

## Introduction and Motivation

Arabic has an incredible degree of syntactic flexibility which makes it difficult to analyze by machines. While continuous multiword expressions (MWEs) are largely solvable by standard sequence labeling models, discontinuous Verbal MWEs (VMWEs) remain a persistent bottleneck due to long-range syntactic gaps.

In this project, we test and evaluate how accurately modern Large Language Models (LLMs) can extract complex, discontinuous Arabic VMWEs when component tokens are separated by intervening words.

## Data

PARSEME-AR 1.3 (PADT / Universal Dependencies treebank format).

## Research Questions

* **RQ1:** How accurately can state-of-the-art LLMs extract complex Arabic verbal expressions (LVCs and VIDs) compared to traditional baseline models?
* **RQ2:** To what extent does the presence of intervening tokens (discontinuity) degrade the extraction accuracy (F1-score) of these models?
* **RQ3:** Does providing few-shot, grammatically structured prompts improve the model's ability to handle highly opaque idioms?

For the detailed experimental roadmap and literature benchmarks, see [ROADMAP.md](ROADMAP.md).

## Setup and usage

### Dependencies

Install dependencies and set up the environment with [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

### Data Preparation

Place the PARSEME-AR 1.3 `.cupt` files inside `data/raw/`:

```text
data/raw/
├── train.cupt
├── dev.cupt
└── test.cupt
```

### Running the Notebook

The exploratory data analysis and extraction pipeline are in `main.ipynb`:

- **VS Code**: Open `main.ipynb` and choose the `.venv` Python kernel.
- **Jupyter Lab**:
  ```bash
  uv run jupyter lab
  ```

