# IMDB Sentiment Analysis (RNN)

A simple RNN-based sentiment analysis model trained on the IMDB movie reviews dataset using Keras/TensorFlow.

## Overview

- Dataset: IMDB reviews (top 10,000 most frequent words)
- Preprocessing: Sequence padding (maxlen=50)
- Model: Embedding → SimpleRNN → Dropout → Dense (sigmoid)
- Training: Binary crossentropy loss, Adam optimizer, with EarlyStopping

## Setup

```bash
pip install -r requirements.txt
```

or, if using `uv`/`pyproject.toml`:

```bash
uv sync
```

## Usage

Open and run the notebook:

```bash
jupyter notebook IMDB_Sentiment_Analysis_RNN.ipynb
```

## Requirements

- Python >= 3.11
- TensorFlow / Keras
- NumPy, Pandas, Matplotlib, scikit-learn