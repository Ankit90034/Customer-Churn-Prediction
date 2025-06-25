import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('churn_model_xgb.pkl')

st.title("Customer Churn Prediction App")

st.subheader("Enter Customer Information")

# User Inputs
gender = st.selectbox('Gender', ['Male', 'Female'])
SeniorCitizen = st.selectbox('Senior Citizen', [0, 1])
Partner = st.selectbox('Partner', ['Yes', 'No'])
Dependents = st.selectbox('Dependents', ['Yes', 'No'])
tenure = st.number_input('Tenure (in months)', min_value=0, max_value=100)
PhoneService = st.selectbox('Phone Service', ['Yes', 'No'])
MultipleLines = st.selectbox('Multiple Lines', ['Yes', 'No', 'No phone service'])
InternetService = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
OnlineSecurity = st.selectbox('Online Security', ['Yes', 'No', 'No internet service'])
OnlineBackup = st.selectbox('Online Backup', ['Yes', 'No', 'No internet service'])
DeviceProtection = st.selectbox('Device Protection', ['Yes', 'No', 'No internet service'])
TechSupport = st.selectbox('Tech Support', ['Yes', 'No', 'No internet service'])
StreamingTV = st.selectbox('Streaming TV', ['Yes', 'No', 'No internet service'])
StreamingMovies = st.selectbox('Streaming Movies', ['Yes', 'No', 'No internet service'])
Contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
PaperlessBilling = st.selectbox('Paperless Billing', ['Yes', 'No'])
PaymentMethod = st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
MonthlyCharges = st.number_input('Monthly Charges', min_value=0.0)
TotalCharges = st.number_input('Total Charges', min_value=0.0)

# Create input dataframe
input_data = {
    'gender': [gender],
    'SeniorCitizen': [SeniorCitizen],
    'Partner': [Partner],
    'Dependents': [Dependents],
    'tenure': [tenure],
    'PhoneService': [PhoneService],
    'MultipleLines': [MultipleLines],
    'InternetService': [InternetService],
    'OnlineSecurity': [OnlineSecurity],
    'OnlineBackup': [OnlineBackup],
    'DeviceProtection': [DeviceProtection],
    'TechSupport': [TechSupport],
    'StreamingTV': [StreamingTV],
    'StreamingMovies': [StreamingMovies],
    'Contract': [Contract],
    'PaperlessBilling': [PaperlessBilling],
    'PaymentMethod': [PaymentMethod],
    'MonthlyCharges': [MonthlyCharges],
    'TotalCharges': [TotalCharges]
}
import pandas as pd
df = pd.DataFrame(input_data)

# Preprocessing (Dummy columns matching training)
df = pd.get_dummies(df)

# Match the model's training features
model_features = model.get_booster().feature_names

for col in model_features:
    if col not in df.columns:
        df[col] = 0

df = df[model_features]

# Prediction
if st.button('Predict Churn'):
    prediction = model.predict(df)
    probability = model.predict_proba(df)[:, 1][0]

    st.subheader('Prediction Result:')
    if prediction[0] == 1:
        st.error(f" Customer is likely to churn with probability {probability*100:.2f}%")
    else:
        st.success(f" Customer is NOT likely to churn with probability {(1-probability)*100:.2f}%")
