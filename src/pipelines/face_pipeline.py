import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st
from src.database.db import get_all_students

@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector() 
    sp = dlib.shape_predictor(face_recognition_models.pose_predictor_model_location())
    facerec = dlib.face_recognition_model_v1(face_recognition_models.face_recognition_model_location())
    return detector, sp, facerec

def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()
    faces = detector(image_np, 1)
    encodings = []

    for face in faces:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1)
        encodings.append(np.array(face_descriptor))
    return encodings

@st.cache_resource
def get_trained_model():
    X = []
    y = []
    student_db = get_all_students()

    if not student_db:
        return None
    
    for student in student_db:
        embedding = student.get('face_embedding')
        if embedding:
            X.append(np.array(embedding))
            y.append(int(student.get('student_id')))

    if len(X) == 0:
        return 0
    
    # Get distinct student count
    unique_classes = len(set(y))
    
    # FIXED: Only train SVM if we have 2 or more distinct students to prevent crashes
    if unique_classes >= 2:
        clf = SVC(kernel='linear', probability=True, class_weight='balanced')
        try:
            clf.fit(X, y)
            return {'clf': clf, 'X': X, 'y': y, 'mode': 'svm'}
        except ValueError:
            return {'X': X, 'y': y, 'mode': 'distance'}
    else:
        return {'X': X, 'y': y, 'mode': 'distance'}

def train_classifier():
    st.cache_resource.clear()
    model_data = get_trained_model()
    return bool(model_data)

def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)
    detected_student = {}
    model_data = get_trained_model()

    if not model_data or model_data == 0:
        return detected_student, [], len(encodings)
    
    X_train = model_data['X']
    y_train = model_data['y']
    mode = model_data['mode']
    all_students = sorted(list(set(y_train)))

    for encoding in encodings:
        if mode == 'svm' and 'clf' in model_data:
            predicted_id = int(model_data['clf'].predict([encoding])[0])
        else:
            # FIXED: Safe Nearest Neighbor fallback matching logic for single-student databases
            distances = [np.linalg.norm(np.array(tx) - encoding) for tx in X_train]
            predicted_id = int(y_train[np.argmin(distances)])

        # FIXED: Look up the vector match distance directly against the classified target vector
        # instead of relying on fragile index tracking
        student_indices = [i for i, label in enumerate(y_train) if label == predicted_id]
        best_match_score = min([np.linalg.norm(np.array(X_train[idx]) - encoding) for idx in student_indices])

        resemblance_threshold = 0.6
        if best_match_score <= resemblance_threshold:
            detected_student[predicted_id] = True

    return detected_student, all_students, len(encodings)