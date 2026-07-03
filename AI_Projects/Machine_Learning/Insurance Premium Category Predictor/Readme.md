# Insurance Premium Category Predictor

A machine learning web app that predicts a user's insurance premium category (**Low / Medium / High**) based on their age, weight, height, income, smoking habit, and occupation.

The project has two parts:
- **Backend** – FastAPI app that serves the ML model (`backend.py`)
- **Frontend** – Streamlit app for user input (`frontend.py`)

## Project Structure

```
.
├── backend.py          # FastAPI backend (model API)
├── frontend.py         # Streamlit frontend (UI)
├── Model.pkl           # Trained ML model
├── insurance.csv        # Dataset used for training
├── Model_training.ipynb # Notebook used to train the model
└── requirements.txt     # Python dependencies
```

## Requirements

- Python 3.9+

## Installation

Create a virtual environment and install the required packages:

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

```bash
pip install fastapi uvicorn streamlit pandas scikit-learn xgboost requests pydantic
```

> Note: On Linux/Mac, activate the environment using `source venv/bin/activate` instead.

## How to Run

### 1. Start the Backend (FastAPI)

```bash
uvicorn backend:app --reload
```

The API will be available at `http://127.0.0.1:8000`.
You can view the interactive API docs at `http://127.0.0.1:8000/docs`.

### 2. Start the Frontend (Streamlit)

Open a **new terminal**, activate the same virtual environment, and run:

```bash
streamlit run frontend.py
```

The app will open in your browser, usually at `http://localhost:8501`.

## Usage

1. Make sure the FastAPI backend is running first.
2. Open the Streamlit app.
3. Enter your details:
   - Age
   - Weight (kg)
   - Height (m)
   - Annual Income (LPA)
   - Smoker (Yes/No)
   - Occupation
4. Click **Predict Premium Category** to get your result (Low / Medium / High).

## API Endpoint

**POST** `/predict`

Example request body:

```json
{
  "age": 30,
  "weigth": 65,
  "height": 1.7,
  "income_lpa": 10,
  "smoker": false,
  "occupation": "private_job"
}
```

Example response:

```json
{
  "prediction_category": "Low"
}
```

## Notes

- The model is trained using the data in `insurance.csv` (see `Model_training.ipynb`).
- `bmi` and `lifestyle_risk` are automatically computed by the backend from user input.