# 🎓 SnapClass AI Attendance System

An AI-powered Smart Attendance Management System that automates student attendance using **Face Recognition**, **Voice Biometrics**, and **Real-Time Attendance Tracking**. Built with **Python**, **Streamlit**, **Supabase**, **Dlib**, and **Machine Learning**, the system eliminates manual attendance processes and provides a seamless classroom experience.

---

## 🚀 Features

### 👤 Face-Based Student Authentication

* Detects student faces from live camera input.
* Generates 128-dimensional facial embeddings using Dlib.
* Matches student identities using Machine Learning classification.
* Supports automatic student recognition during attendance.

### 🎙️ Voice Enrollment & Recognition

* Optional voice enrollment during student registration.
* Generates unique voice embeddings for identity verification.
* Enables voice-assisted attendance workflows.

### 📚 Subject Management

* Create and manage classroom subjects.
* Student enrollment into subjects.
* Subject-wise attendance tracking and management.

### 📝 Automated Attendance Recording

* Real-time attendance marking using AI models.
* Eliminates manual attendance sheets.
* Reduces attendance fraud and proxy attendance.

### ☁️ Cloud Database Integration

* Secure student and attendance data storage using Supabase.
* Fast retrieval of attendance history and student information.
* Scalable backend architecture.

### 📊 Dashboard & Analytics

* Student attendance history.
* Subject-wise attendance records.
* Attendance monitoring and management tools.

---

## 🏗️ System Architecture

```text
Student Camera Input
         │
         ▼
 Face Detection (Dlib)
         │
         ▼
 Face Embedding Generation
         │
         ▼
 SVM Classification Model
         │
         ▼
 Student Identification
         │
         ▼
 Attendance Recording
         │
         ▼
      Supabase
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Database

* Supabase

### Machine Learning

* Dlib
* Scikit-Learn (SVM)
* NumPy

### Computer Vision

* OpenCV
* Face Recognition Models

### Voice Processing

* Resemblyzer
* Librosa

---

## 📂 Project Structure

```text
SnapClass-AI-Attendance/

├── app.py
├── requirements.txt
├── .streamlit/
│   └── config.toml
│
├── src/
│   ├── components/
│   ├── database/
│   │   ├── config.py
│   │   └── db.py
│   │
│   ├── pipelines/
│   │   ├── face_pipeline.py
│   │   └── voice_pipeline.py
│   │
│   ├── screens/
│   │   ├── home_screen.py
│   │   ├── student_screen.py
│   │   └── teacher_screen.py
│   │
│   └── ui/
│       └── base_layout.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/AtishayJain458/SnapClass-AI-Attendance_project.git
cd SnapClass-AI-Attendance_project
```

### Create Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Configure Environment Variables

Add your Supabase credentials:

```env
SUPABASE_URL=your_project_url
SUPABASE_KEY=your_anon_key
```

### Run Application

```bash
streamlit run app.py
```

---

## 🤖 Machine Learning Workflow

### Face Recognition Pipeline

1. Capture image from camera.
2. Detect face using Dlib face detector.
3. Generate facial landmarks.
4. Extract 128-dimensional face embeddings.
5. Train SVM classifier on registered student embeddings.
6. Predict student identity.
7. Record attendance.

### Voice Recognition Pipeline

1. Record student voice sample.
2. Extract voice embeddings.
3. Store embeddings in database.
4. Compare embeddings during verification.

---

## 🎯 Business Impact

* Reduces manual attendance effort.
* Minimizes proxy attendance.
* Improves classroom efficiency.
* Enables digital attendance records.
* Supports scalable classroom management.

---

## 🔮 Future Enhancements

* Multi-face attendance marking.
* Attendance analytics dashboard.
* QR-based backup attendance.
* Mobile application support.
* Real-time notification system.
* Deep Learning-based face recognition models.

---

## 👨‍💻 Author

**Atishay Jain**

AI/ML Engineer | Data Science Enthusiast

* LinkedIn: https://linkedin.com/in/atishay457
* GitHub: https://github.com/AtishayJain457

---

⭐ If you found this project useful, consider giving it a star.
