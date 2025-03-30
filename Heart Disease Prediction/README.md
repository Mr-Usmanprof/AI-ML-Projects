# Heart Disease Prediction using Neural Networks

## 📌 Project Overview
This project predicts the likelihood of heart disease using a neural network model built with TensorFlow and Keras. By leveraging patient health data, the model assists in early detection and diagnosis, potentially improving healthcare outcomes.

## 🚀 Features
- Data Preprocessing (Feature Scaling using StandardScaler)
- Neural Network Model Implementation using Keras Sequential API
- Performance Evaluation using Accuracy and Confusion Matrix
- Predictive Analysis for Heart Disease Diagnosis

## 🛠️ Technologies Used
- Python
- TensorFlow & Keras
- Scikit-learn
- Pandas & NumPy
- Matplotlib

## 📊 Dataset Information
The dataset contains various medical attributes related to heart disease, including:
- **Age**: Age of the patient
- **Sex**: Gender of the patient
- **Chest Pain Type**: Different types of chest pain experienced
- **Resting Blood Pressure**: Patient's blood pressure
- **Cholesterol Level**: Serum cholesterol levels
- **Fasting Blood Sugar**: Blood sugar levels
- **Resting ECG Results**: Electrocardiographic results
- **Max Heart Rate Achieved**: Maximum heart rate during exercise
- **Exercise-Induced Angina**: Chest pain due to exercise
- **ST Depression & Slope**: ECG-related attributes
- **Target**: Presence (1) or Absence (0) of Heart Disease

## 🏗️ Model Architecture
The neural network consists of three layers:
1. **Input Layer**: 13 features with ReLU activation
2. **Hidden Layer**: 14 neurons with ReLU activation
3. **Output Layer**: 1 neuron with Sigmoid activation for binary classification

The model is compiled using:
- **Optimizer**: Adam
- **Loss Function**: Binary Crossentropy
- **Batch Size**: 8
- **Epochs**: 100

## 🏠 Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/Mr-Usmanprof/Heart_Disease_Prediction.git
   cd Heart_Disease_Prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook to train and evaluate the model.

## 📈 Results & Insights
The neural network model achieves an **accuracy of 84%**, indicating strong predictive capability for heart disease diagnosis.

## 🤝 Contact
For collaboration, feel free to reach out:
- **Email:** [mr.usmanprof@gmail.com](mailto:mr.usmanprof@gmail.com)
- **LinkedIn:** [Muhammad Usman](https://www.linkedin.com/in/muhammad-usman-freelance)

---
**⭐ Star this repository if you find it useful!**
