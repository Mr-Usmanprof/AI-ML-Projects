import streamlit as st
import requests

st.set_page_config(page_title="Churn Predictor", layout="centered")
st.title("🔍 Customer Churn Prediction")

# Form to take user input
with st.form("churn_form"):
    gender = st.selectbox("Gender", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    Partner = st.selectbox("Partner", [0, 1])
    Dependents = st.selectbox("Dependents", [0, 1])
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    PhoneService = st.selectbox("Phone Service", [0, 1])
    MultipleLines = st.selectbox("Multiple Lines", [0, 1])
    InternetService = st.selectbox("Internet Service", [0, 1, 2], format_func=lambda x: ["No", "DSL", "Fiber"][x])
    OnlineSecurity = st.selectbox("Online Security", [0, 1])
    OnlineBackup = st.selectbox("Online Backup", [0, 1])
    DeviceProtection = st.selectbox("Device Protection", [0, 1])
    TechSupport = st.selectbox("Tech Support", [0, 1])
    StreamingTV = st.selectbox("Streaming TV", [0, 1])
    StreamingMovies = st.selectbox("Streaming Movies", [0, 1])
    Contract = st.selectbox("Contract", [0, 1, 2], format_func=lambda x: ["Month-to-month", "One year", "Two year"][x])
    PaperlessBilling = st.selectbox("Paperless Billing", [0, 1])
    PaymentMethod = st.selectbox("Payment Method", [0, 1, 2, 3], format_func=lambda x: ["Electronic check", "Mailed check", "Bank transfer", "Credit card"][x])
    MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=70.0)
    TotalCharges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=1000.0)
    HasPhone = st.selectbox("Has Phone", [0, 1])

    submit = st.form_submit_button("📤 Predict")

# Make prediction
if submit:
    input_data = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges,
        "HasPhone": HasPhone
    }

    try:
        res = requests.post("http://127.0.0.1:8000/predict", json=input_data)
        st.write("✅ Response status code:", res.status_code)
        if res.status_code == 200:
            result = res.json()
            churn_label = "⚠️ Customer is likely to churn!" if result['churn'] == 1 else "✅ Customer will likely stay."
            st.subheader("Prediction Result:")
            st.success(churn_label)
        else:
            st.error(f"❌ Error: {res.status_code}")
            st.code(res.text)
    except Exception as e:
        st.error("❌ Request failed. Is FastAPI running?")
        st.exception(e)


