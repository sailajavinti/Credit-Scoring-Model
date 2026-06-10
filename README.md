# Credit Scoring Prediction System

## Overview

This project predicts an individual's creditworthiness using Machine Learning techniques. The model analyzes financial and demographic information such as income, debts, payment history, credit score, savings, and existing loans to determine whether an applicant is a good or bad credit risk.

## Live Demo

Streamlit App: https://credit-scoring-model-3tqbvraqfbmwqos2cp7njf.streamlit.app/

## GitHub Repository

Source Code: https://github.com/sailajavinti/Credit-Scoring-Model


## Objectives

* Predict customer creditworthiness.
* Compare multiple machine learning algorithms.
* Perform feature engineering to improve model performance.
* Evaluate models using standard classification metrics.
* Build a user-friendly prediction interface using Streamlit.

## Dataset

A synthetic credit scoring dataset containing 10,000 records was used for this project.

### Features

* Age
* EmploymentYears
* Income
* Debts
* LoanAmount
* CreditCards
* LatePayments
* PaymentHistory
* CreditScore
* ExistingLoans
* Savings
* Dependents
* DebtIncomeRatio
* LoanIncomeRatio
* FinancialStress
* SavingsIncomeRatio
* IncomePerLoan

### Target Variable

* Creditworthy

  * 1 = Good Credit Risk
  * 0 = Bad Credit Risk

## Feature Engineering

Additional features were created to improve predictive performance:

* DebtIncomeRatio
* LoanIncomeRatio
* FinancialStress
* SavingsIncomeRatio
* IncomePerLoan

## Machine Learning Models

The following algorithms were trained and compared:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

## Model Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC Score
* Confusion Matrix

## Hyperparameter Tuning

Random Forest hyperparameters were optimized using GridSearchCV / RandomizedSearchCV to improve performance.

## Explainable AI

SHAP (SHapley Additive exPlanations) was used to understand feature importance and explain model predictions.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* SHAP
* Joblib
* Streamlit

## Project Structure

Credit-Scoring-Model/

├── Credit_Scoring_Model.ipynb

├── credit_scoring_final.csv

├── credit_model.pkl

├── streamlit_app.py

├── requirements.txt

└── README.md

## Results

The Random Forest model achieved the best performance and was selected as the final model for deployment.

## Future Improvements

* Integration with real-world credit datasets.
* Advanced ensemble models such as XGBoost.
* Real-time credit risk monitoring dashboard.
* Cloud deployment and API integration.

## Author

Sailaja Vinti
Machine Learning Intern – CodeAlpha
