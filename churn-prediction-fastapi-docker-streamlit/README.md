# 🔁 Customer Churn Prediction System  
**FastAPI + Streamlit + Docker-based End-to-End ML Deployment**  

## 📌 Project Overview  
Customer churn prediction helps telecom and subscription-based businesses understand why users leave and which customers are at risk. This solution leverages machine learning to:  
- 🔍 Predict churn based on customer behavior  
- 📈 Improve retention strategies with data insights  
- 🚀 Deploy with a clean UI and production-ready backend  

---

## 🛠 Tech Stack  
| Layer              | Tool / Framework           |
|--------------------|----------------------------|
| Backend API        | FastAPI                    |
| Frontend           | Streamlit                  |
| Containerization   | Docker                     |
| Language           | Python                     |
| Model Persistence  | Pickle (`.pkl`)            |
| ML Algorithm       | Logistic Regression / Random Forest |

---

## 📂 Project Structure  
```
churn-prediction/
│
├── api/                     # FastAPI app
│   ├── main.py              # API server
│   └── model.pkl            # Trained model
│
├── streamlit_app/           # Streamlit frontend
│   └── app.py               # UI application
│
├── Dockerfile               # Docker build instructions
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🚀 Running Locally

### ✅ Step 1: Clone the Repository  
```bash
git clone https://github.com/Mr-Usmanprof/churn-prediction-fastapi-docker-streamlit.git
cd churn-prediction-fastapi-docker-streamlit
```

### ✅ Step 2: Build Docker Image  
```bash
docker build -t churn-api .
```

### ✅ Step 3: Run Docker Container  
```bash
docker run -d --name churn_container -p 8000:8000 churn-api
```

### ✅ Step 4: Run Streamlit UI (from host)  
```bash
streamlit run streamlit_app/app.py
```

---

## 🔁 API Endpoint  

| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| POST   | `/predict`       | Returns churn prediction |

### Example Input JSON  
```json
{
  "gender": 1,
  "SeniorCitizen": 0,
  "Partner": 1,
  "Dependents": 0,
  "tenure": 24,
  "PhoneService": 1,
  "MultipleLines": 1,
  "InternetService": 1,
  "OnlineSecurity": 1,
  "OnlineBackup": 1,
  "DeviceProtection": 0,
  "TechSupport": 1,
  "StreamingTV": 1,
  "StreamingMovies": 0,
  "Contract": 2,
  "PaperlessBilling": 1,
  "PaymentMethod": 2,
  "MonthlyCharges": 65.35,
  "TotalCharges": 1578.90,
  "HasPhone": 1
}
```

---

## 📈 Model Details  
- Trained on customer churn dataset  
- Preprocessing includes label encoding, feature scaling  
- Saved with `joblib` or `pickle`  
- Logistic Regression and RandomForestClassifier tested  
- Accuracy: ~80–85% on validation set  

---

## 📦 Docker Hub  
👉 Image: [mrusmanprof/churn-api](https://hub.docker.com/repository/docker/mrusmanprof/churn-api)

---

## 💼 Why This Project Matters  
This project demonstrates:  
- Full cycle ML system from training to deployment  
- Building APIs with FastAPI  
- Streamlit for rapid UI development  
- Docker for containerization and portability  
- Skill in data science + devops + app integration  

---

## 💌 Contact  
**Muhammad Usman**  
📧 [mr.usmanprof@gmail.com](mailto:mr.usmanprof@gmail.com)  
🌐 [LinkedIn](https://www.linkedin.com/in/muhammad-usman-freelance)  
💻 GitHub: [Mr-Usmanprof](https://github.com/Mr-Usmanprof)  

---

⭐ **If you liked this project, please give it a star!** ⭐  


   
   

