# 🎓 SnapClass AI Attendance System

An AI-powered Smart Attendance Management System that automates student attendance using Face Recognition, Voice Biometrics, and Cloud-Based Data Management.

Built using Python, Streamlit, Dlib, Scikit-Learn, Supabase, and Resemblyzer, the system eliminates manual attendance processes and provides an efficient, secure, and scalable attendance solution for educational institutions.

---

## 🚀 Features

### 👤 Face Recognition Attendance

* Detects student faces using Dlib Face Detector.
* Generates 128-dimensional facial embeddings.
* Identifies students using an SVM (Support Vector Machine) classifier.
* Automatically marks attendance for recognized students.

### 🎙️ Voice Enrollment & Verification

* Optional voice enrollment during student registration.
* Generates unique voice embeddings using Resemblyzer.
* Supports voice-based identity verification.

### 📚 Subject Management

* Create and manage classroom subjects.
* Student enrollment into subjects.
* Subject-wise attendance tracking.

### 📱 QR-Based Subject Sharing

* Generate QR codes for subject enrollment.
* Easy classroom onboarding.
* Quick subject access for students.

### ☁️ Cloud Database Integration

* Stores student profiles and attendance records in Supabase.
* Real-time data access and management.
* Scalable backend architecture.

### 🔐 Secure Authentication

* Password hashing using Bcrypt.
* Secure storage of user credentials.
* Protection against plain-text password storage.

---

## 🏗️ System Architecture

```text
Student Camera Input
        │
        ▼
 Face Detection (Dlib)
        │
        ▼
 Face Landmark Extraction
        │
        ▼
 128-D Face Embeddings
        │
        ▼
 SVM Classification
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

* Scikit-Learn (SVM)
* Dlib

### Face Recognition

* Dlib Face Recognition Models

### Voice Recognition

* Resemblyzer

### Audio Processing

* Librosa

### Image Processing

* Pillow (PIL)

### Data Processing

* NumPy
* Pandas

### Authentication & Security

* Bcrypt

### QR Code Generation

* Segno

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
│   │   ├── dialog_add_photo.py
│   │   ├── dialog_attendance_results.py
│   │   ├── dialog_auto_enroll.py
│   │   ├── dialog_create_subject.py
│   │   ├── dialog_enroll.py
│   │   ├── dialog_share_subject.py
│   │   ├── dialog_voice_attendance.py
│   │   ├── footer.py
│   │   ├── header.py
│   │   └── subject_card.py
│   │
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

## 🤖 AI Workflow

### Face Recognition Pipeline

1. Capture image using device camera.
2. Detect faces using Dlib Face Detector.
3. Extract facial landmarks.
4. Generate 128-dimensional face embeddings.
5. Train SVM classifier using stored student embeddings.
6. Predict student identity.
7. Mark attendance automatically.

### Voice Recognition Pipeline

1. Record student voice sample.
2. Generate voice embeddings using Resemblyzer.
3. Store embeddings in Supabase.
4. Verify identity using voice similarity.

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/AtishayJain458/SnapClass-AI-Attendance_project.git
cd SnapClass-AI-Attendance_project
```

### Create Virtual Environment

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

### Configure Supabase

Create a `.env` file and add:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
```

### Run Application

```bash
streamlit run app.py
```

---

## 🎯 Key Highlights

* Automated attendance using AI-powered face recognition.
* 128-dimensional facial embedding extraction.
* SVM-based student classification.
* Voice-assisted attendance support.
* Cloud-based attendance management using Supabase.
* QR-based subject enrollment system.
* Secure authentication with password hashing.
* Interactive Streamlit user interface.

---

## 📈 Future Improvements

* Multi-face attendance detection.
* Attendance analytics dashboard.
* Mobile application integration.
* Deep Learning-based face recognition models.
* Real-time attendance notifications.
* Attendance report export functionality.

---

## 👨‍💻 Author

### Atishay Jain

AI/ML Engineer | Machine Learning Enthusiast | Data Science Learner

📧 [atishayyjain.45@gmail.com](mailto:atishayyjain.45@gmail.com)

🔗 LinkedIn: https://linkedin.com/in/atishay457

💻 GitHub: https://github.com/AtishayJain458

---

⭐ If you found this project useful, please consider giving it a star.
