# 🚗 Fuel Efficiency Prediction using TensorFlow

Predicting fuel efficiency (miles per gallon - MPG) is crucial in automotive engineering and environmental sustainability. This project uses the **Auto MPG dataset** to build and train a deep learning model using **TensorFlow** for predicting vehicle MPG based on features like engine size, weight, and horsepower.

## 📌 Project Overview

This repository demonstrates a complete deep learning workflow to predict fuel efficiency using:

- 📊 **Exploratory Data Analysis (EDA)**
- 🧹 **Data Cleaning and Preprocessing**
- 🔁 **Train/Test Splits**
- 🧠 **Model Building using TensorFlow & Keras**
- 📈 **Training and Evaluation**

## 🛠 Technologies Used

- Python 3.11
- Pandas, NumPy, Seaborn, Matplotlib
- Scikit-learn
- TensorFlow / Keras

## 📂 Dataset

We use the **Auto MPG dataset**, which contains 398 entries and 9 columns, including:

- `mpg`: target variable (Miles per Gallon)
- `cylinders`, `horsepower`, `weight`, `acceleration`, etc.: features
- `car name`: ignored in modeling


## 📈 Model Architecture

- Input Layer (6 features)
- Dense (256 units) + ReLU
- BatchNormalization
- Dense (256 units) + ReLU
- Dropout (rate = 0.3)
- BatchNormalization
- Output Layer (1 unit) + ReLU

Optimizer: `adam`  
Loss: `Mean Absolute Error (MAE)`  
Metrics: `Mean Absolute Percentage Error (MAPE)`

## 📊 Results

The model is trained for **50 epochs** and achieves good generalization performance with low MAPE. The final loss and metric trends are plotted for interpretation.

## 📌 Folder Structure

├── auto-mpg.csv # Dataset file ├── fuel_efficiency_model.ipynb # Jupyter Notebook with full code ├── README.md # Project documentation

## 🏗️ Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/Mr-Usmanprof/Credit_Card_Fraud_Detection.git
   cd Credit_Card_Fraud_Detection
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook to train and evaluate the model.

## 🤝 Contact
For collaboration feel free to reach out:
- **Email:** [mr.usmanprof@gmail.com](mailto:mr.usmanprof@gmail.com)
- **LinkedIn:** [Muhammad Usman](https://www.linkedin.com/in/muhammad-usman-freelance)

---
**⭐ Star this repository if you find it useful!**
