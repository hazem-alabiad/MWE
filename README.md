# Arabic Verbal Multiword Expressions (VMWEs) and LLMs

## Introduction and motivation

Arabic has an incredible degree of flexibility which makes it difficult to analyze by machines. So far, many of the NLP tasks such as Named Entity Recognition (NER) and continuos MWE are solved, we still struggle with discontinuous VMWEs.
In this project, we aim to test and evaluate how accurately LLM can catch these VMWEs especially when they have lots of intervening words in between (discontinuity).

## Data

PARSEME-AR 1.3

## Research Questions

1. How well the SOTA LLMs can catch VMWEs in Arabic?
2. Does the intervening words downgrade the performance of the LLM detecting VMWEs (discontinuity )?
3. Does providing a few shots help the LLM detect the VMWEs better compared to zero-shot?

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

