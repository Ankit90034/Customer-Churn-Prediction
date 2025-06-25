# Customer-Churn-Prediction

### Project Overview
This project predicts customer churn for a telecom company using machine learning. It combines SQL for data handling, Python for building the machine learning model, and Streamlit for web-based deployment.

The objective is to identify customers who are likely to discontinue services, helping the business take proactive retention actions.

### Dataset
- Source: Kaggle - Telco Customer Churn Dataset
- Records: ~7,000 customers
- Features: 21 attributes (demographics, service usage, payment details)

### Key Features
- CustomerID
- Gender
- SeniorCitizen
- Partner
- Dependents
- Tenure
- PhoneService
- InternetService
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies
- Contract
- PaperlessBilling
- PaymentMethod
- MonthlyCharges
- TotalCharges
- Churn (Target Variable

### Features
 SQL: Data import, cleaning, null handling, basic analysis.

 Machine Learning: Churn prediction using XGBoost Classifier.

 Web App: Interactive Streamlit app for making predictions.

 Deployment: Temporarily hosted using ngrok/LocalTunnel from Google Colab.

### Tech Stack
- Python
- Numpy
- Pandas
- Matplotlib
- Seaborn
- Sckit-learn
- XGBoost
- Streamlit
- Ngrok
