import streamlit as st
import joblib
import requests  # Library to make HTTP requests

# Load the trained model from GitHub
model_url = 'https://raw.githubusercontent.com/your_username/your_repository/main/loan_approval_model.joblib'
response = requests.get(model_url)
with open('loan_approval_model.joblib', 'wb') as f:
    f.write(response.content)

# Load the model
model = joblib.load('loan_approval_model.joblib')

def check_loan_approval(income, loan_amount):
    # Preprocess input features as needed
    # For simplicity, we'll use the same preprocessing steps as in the training code

    # Example preprocessing:
    # income_scaled = (income - mean_income) / std_income
    # loan_amount_scaled = (loan_amount - mean_loan_amount) / std_loan_amount

    # Make prediction using the loaded model
    prediction = model.predict([[income, loan_amount]])[0]

    # Map prediction to result message
    result = 'Loan Approved!' if prediction == 1 else 'Loan Rejected.'

    return result

def main():
    st.title('Loan Approval Checker')

    # Get user inputs
    income = st.number_input('Enter your income:', min_value=0)
    loan_amount = st.number_input('Enter the loan amount:', min_value=0)

    # Check loan approval when the user clicks the button
    if st.button('Check Loan Approval'):
        result = check_loan_approval(income, loan_amount)
        st.success(result)

if __name__ == '__main__':
    main()
