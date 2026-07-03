# Placement Predictor

This is a simple Machine Learning project that predicts whether a student is likely to get placed (get a job) based on their **CGPA** and **IQ**.

## Project Overview

In this project, we trained a **Logistic Regression** model that takes two features as input:
- **CGPA** (ranging from 0 to 10)
- **IQ**

And produces one of the following outputs:
-  The student is likely to get placed
-  The student is unlikely to get placed

The model has been deployed using **Streamlit** as a simple web app, where users can enter their CGPA and IQ to get a prediction.

## Files in this Project

| File | Description |
|------|-------------|
| `Placement_end_to_end_ml.ipynb` | Notebook containing the complete code for loading data, cleaning, EDA, model training, and exporting the model (`model.pkl`) |
| `placement.csv` | Dataset containing CGPA, IQ, and placement status |
| `model.pkl` | Trained Logistic Regression model (pickle format) |
| `app.py` | Streamlit app that loads the model and generates predictions |
| `requirements.txt` | Python libraries required for this project |

## How to Run This Project

### 1. Clone the repository to your computer
```bash
git clone <your-repo-link>
cd placement_predictor
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate   # Mac/Linux
```

### 3. Install the required libraries
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

The app will open automatically in your browser (if it doesn't, open the link shown in the terminal).

## How to Use the App

1. Enter your **CGPA** (between 0 and 10)
2. Enter your **IQ**
3. Click the **Predict** button
4. The app will tell you whether the student is likely to be placed or not

## Model Details

- **Algorithm:** Logistic Regression
- **Input Features:** CGPA, IQ
- **Output:** Placement (1 = Placed, 0 = Not Placed)
- **Accuracy:** ~90% (on test data)

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit

## Future Improvements

- Add more features (e.g., communication skills, internships, projects)
- Try different models (Random Forest, XGBoost) for better accuracy
- Improve the app's UI

