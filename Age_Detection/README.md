# Age Detection using Deep Learning

## 📌 Project Overview
This project detects faces in an image and predicts the estimated age of a person using a pre-trained deep learning model. It utilizes OpenCV's DNN module with a Caffe-based model for age estimation and Dlib for face detection.

## 🚀 Features
- Face Detection using Dlib
- Age Prediction using a Caffe pre-trained model
- Image Preprocessing with OpenCV
- Real-time age classification

## 🛠️ Technologies Used
- Python
- OpenCV
- Dlib
- NumPy
- Deep Learning (Caffe Model)

## 🏗️ Model Details
The project uses a pre-trained age detection model:
- **Model Architecture:** Caffe-based deep learning model
- **Age Categories:**
  - (0-2)
  - (4-6)
  - (8-12)
  - (15-20)
  - (25-32)
  - (38-43)
  - (48-53)
  - (60-100)
- **Preprocessing:** Input images are resized to (227x227) with mean subtraction before prediction.

## 🏠 Installation & Usage
### Prerequisites
- Python 3.8+
- OpenCV
- Dlib
- Pre-trained age detection model files:
  - `age_net.caffemodel`
  - `age_deploy.prototxt`

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Mr-Usmanprof/Age-Detection.git
   cd Age-Detection
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place an image (`usman.jpg`) in the working directory.
4. Run the script:
   ```bash
   python age_detection.py
   ```

## 📈 Results & Insights
The system successfully detects faces and predicts the approximate age category with high accuracy using the pre-trained model.

## 🤝 Contact
For collaboration, feel free to reach out:
- **Email:** [mr.usmanprof@gmail.com](mailto:mr.usmanprof@gmail.com)
- **LinkedIn:** [Muhammad Usman](https://www.linkedin.com/in/muhammad-usman-freelance)

---
**⭐ Star this repository if you find it useful!**
