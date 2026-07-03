# Spam Classifier ML Pipeline (DVC)

A simple end-to-end machine learning pipeline that classifies SMS/Email messages as **Spam** or **Not Spam**, built using **DVC (Data Version Control)** for pipeline and experiment tracking.

## Project Structure

```
.
├── src/
│   ├── data_ingestion.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_building.py
│   └── model_evaluation.py
├── params.yaml
├── dvc.yaml
└── dvc.lock
```

## Pipeline Stages

1. **Data Ingestion** – Downloads the raw spam dataset, cleans it, and splits it into train/test sets.
2. **Data Preprocessing** – Cleans text data: lowercasing, tokenization, stopword removal, and stemming.
3. **Feature Engineering** – Converts text into numerical features using TF-IDF.
4. **Model Building** – Trains a Random Forest classifier on the TF-IDF features.
5. **Model Evaluation** – Evaluates the model using accuracy, precision, recall, and AUC, with metrics logged via DVCLive.

## Tech Stack

- Python
- Pandas, Scikit-learn, NLTK
- DVC & DVCLive
- Random Forest Classifier

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Reproduce the full pipeline:
   ```bash
   dvc repro
   ```

3. View experiment metrics:
   ```bash
   dvc exp show
   ```

## Configuration

All parameters (test size, max features, model hyperparameters) are managed in `params.yaml`, making the pipeline easy to tune without changing code.

## Notes

- Logs for each stage are generated automatically in the `logs/` folder.
- Trained model and evaluation metrics are saved in `models/` and `reports/`.