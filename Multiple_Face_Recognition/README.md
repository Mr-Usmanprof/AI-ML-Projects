# 👥 Multiple Face Recognition using Deep Learning

This project focuses on building a **Multiple Face Recognition System** that detects and identifies multiple faces in real-time images or video streams using deep learning and computer vision techniques.

---

## 🧠 Project Overview

The system detects human faces from an input image or camera feed and recognizes each person based on learned embeddings. It leverages **face detection** and **face recognition** pipelines to accurately identify individuals even in group settings.

---

## 📌 Key Features

- 📸 Detects **multiple faces** in a single frame  
- 🧬 Extracts face embeddings using pre-trained deep learning models  
- 🏷️ Identifies individuals using similarity matching  
- 🖥️ Real-time performance on images or webcam  
- 🔁 Easily updatable face database for new identities  

---

## 🛠️ Technologies Used

- **Language**: Python  
- **Libraries**:  
  - `OpenCV` – Image processing and real-time camera access  
  - `Dlib` – Face detection and landmark prediction  
  - `face_recognition` – Face embeddings and matching  
  - `NumPy`, `os` – Utilities and file management  

---

## 🔍 How It Works

1. **Face Detection**  
   Detects faces using HOG (Histogram of Oriented Gradients) or CNN-based models.

2. **Feature Extraction**  
   Converts each face into a 128-dimensional embedding using `face_recognition`.

3. **Face Recognition**  
   Compares embeddings to a database of known faces using Euclidean distance.

4. **Labeling**  
   Labels each detected face in the image or video with the matched identity.

---

## 🧪 Demo Workflow

```bash
# Step 1: Prepare known faces
📁 known_faces/
   ├── person1/
   │   └── img1.jpg
   └── person2/
       └── img2.jpg

# Step 2: Run face recognition on an image
$ python recognize_faces.py --input path/to/image.jpg

# OR run on live webcam feed
$ python recognize_faces.py --webcam
```

---

## 📈 Applications

- 🎓 Attendance systems  
- 🛡️ Security and surveillance  
- 🏷️ Automated photo tagging  
- 🔐 Access control in smart systems  

---

## 🤝 Contact

For collaboration, inquiries, or to discuss any of the projects I have worked on, feel free to reach out:

- **Email**: [mr.usmanprof@gmail.com](mailto:mr.usmanprof@gmail.com)  
- **LinkedIn**: [Muhammad Usman](https://www.linkedin.com/in/muhammad-usman-freelance)

---

## 🔮 Looking Ahead

I am passionate about solving real-world problems using AI and Machine Learning. This project reflects my growing experience in computer vision and deep learning, and I'm eager to take on more advanced challenges ahead.

---

**⭐ Star this repository if you find it useful!**
