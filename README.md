# 😄 Mood Detection Tool (Python + OpenCV)

## 📌 Overview

A Python project that detects human mood (Happy vs Neutral/Sad) using OpenCV's Haar cascades.  
Users can choose between processing a single image or live webcam feed.

- Detect faces in images or live video  
- Detect smiles inside faces  
- Annotate mood on the face  
- Save processed images or webcam video  

This is an interactive project for learning real-time computer vision applications.

---

## 🚀 Key Features

- **Image input mode** with mood detection  
- **Live webcam mode** with optional video recording  
- Detect **faces** using Haar cascades  
- Detect **smiles** to determine mood  
- Annotate **Happy** or **Neutral/Sad** above each face  
- Save processed image or video output  
- Simple menu-driven interface  

---

## 🛠 Technologies Used

- Python  
- OpenCV  
- NumPy  

---

## 🔎 How It Works

### 1️⃣ Face & Smile Detection
- Uses OpenCV Haar cascade classifiers:
  - `haarcascade_frontalface_default.xml`  
  - `haarcascade_smile.xml`  
- Faces are detected in grayscale images.  
- Smiles are detected inside each face region.  

### 2️⃣ Mood Annotation
- If smile(s) detected → **Happy**  
- Else → **Neutral/Sad**  
- Text is drawn above the face rectangle using `cv2.putText`.

### 3️⃣ Image Mode
1. User inputs the path of the image  
2. Image is processed to detect faces and mood  
3. Annotated image is displayed  
4. Image is saved as `mood_detected.jpg`

### 4️⃣ Webcam Mode
1. Accesses the default webcam  
2. Real-time mood detection for each frame  
3. Optionally save webcam output as `webcam_mood_detected.mp4`  
4. Press `q` to quit  

---

## 📦 Installation

Install required packages:
```bash
pip install opencv-python numpy
