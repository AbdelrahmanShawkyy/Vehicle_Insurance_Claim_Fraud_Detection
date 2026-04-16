# Vehicle Insurance Claim Fraud Detection

An end-to-end machine learning project designed to detect fraudulent insurance claims. This project covers the full ML lifecycle: from Data Exploration and Feature Engineering to Model Deployment using a modern tech stack.

## Key Features
* **EDA & Analysis:** Comprehensive data exploration to identify patterns in fraudulent behavior.
* **Predictive Modeling:** Trained using **XGBoost** with a focus on handling class imbalance.
* **FastAPI Backend:** A robust REST API to serve model predictions in real-time.
* **Streamlit Frontend:** An interactive, user-friendly dashboard for manual claim analysis.
* **Professional UI:** Custom CSS styling for an enhanced user experience.

## Tech Stack
* **Language:** Python 3.x
* **ML Libraries:** Pandas, Scikit-learn, XGBoost, Imbalanced-learn (SMOTE).
* **Backend:** FastAPI, Uvicorn.
* **Frontend:** Streamlit.
* **Deployment Tools:** Pickle (for model serialization).

## Project Structure
```text
├── api/
│   ├── main.py              # FastAPI server
│   ├── best_fraud_model.pkl # Trained XGBoost model
│   └── model_columns.pkl   # Saved feature columns
├── frontend/
│   └── app.py               # Streamlit UI code
├── notebooks/
│   └── Vehicle_Insurance_Fraud_Detection.ipynb # Full ML workflow
├── data/
│   └── insurance_claims.csv # Dataset
└── README.md


# Navigate to api folder
cd api

# Start the server
uvicorn main:app --reload
