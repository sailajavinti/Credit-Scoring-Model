import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("credit_model.pkl")

st.set_page_config(page_title="Credit Scoring System")

st.title("💳 Credit Scoring Prediction System")
st.write("Predict whether a customer is creditworthy.")

# User Inputs
income = st.number_input("Income", min_value=0.0)
debts = st.number_input("Debts", min_value=0.0)
late_payments = st.number_input("Late Payments", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0.0)

age = st.number_input("Age", min_value=18, max_value=100)
employment_years = st.number_input("Employment Years", min_value=0)

credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=850
)

savings = st.number_input("Savings", min_value=0.0)

existing_loans = st.number_input(
    "Existing Loans",
    min_value=0
)

credit_cards = st.number_input(
    "Credit Cards",
    min_value=0
)

dependents = st.number_input(
    "Dependents",
    min_value=0
)

payment_history = st.selectbox(
    "Payment History",
    ["Average", "Excellent", "Good", "Poor"]
)

# Feature Engineering
debt_income_ratio = debts / income if income > 0 else 0
loan_income_ratio = loan_amount / income if income > 0 else 0

financial_stress = (
    debt_income_ratio * 100 +
    late_payments * 5
)

savings_income_ratio = (
    savings / income if income > 0 else 0
)

income_per_loan = (
    income / (existing_loans + 1)
)

# One-Hot Encoding
payment_excellent = 1 if payment_history == "Excellent" else 0
payment_good = 1 if payment_history == "Good" else 0
payment_poor = 1 if payment_history == "Poor" else 0

if st.button("Predict Creditworthiness"):

    data = pd.DataFrame([[
        income,
        debts,
        late_payments,
        loan_amount,
        age,
        employment_years,
        credit_score,
        savings,
        existing_loans,
        credit_cards,
        dependents,
        debt_income_ratio,
        loan_income_ratio,
        financial_stress,
        savings_income_ratio,
        income_per_loan,
        payment_excellent,
        payment_good,
        payment_poor
    ]], columns=[
        'Income',
        'Debts',
        'LatePayments',
        'LoanAmount',
        'Age',
        'EmploymentYears',
        'CreditScore',
        'Savings',
        'ExistingLoans',
        'CreditCards',
        'Dependents',
        'DebtIncomeRatio',
        'LoanIncomeRatio',
        'FinancialStress',
        'SavingsIncomeRatio',
        'IncomePerLoan',
        'PaymentHistory_Excellent',
        'PaymentHistory_Good',
        'PaymentHistory_Poor'
    ])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1] * 100

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")

    st.write(f"### Creditworthiness Score: {probability:.2f}%")

    if probability >= 80:
        st.info("Risk Level: Low Risk")
    elif probability >= 60:
        st.warning("Risk Level: Medium Risk")
    else:
        st.error("Risk Level: High Risk")
