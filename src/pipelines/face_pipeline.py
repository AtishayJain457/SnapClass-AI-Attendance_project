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
        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1) # 128 embedding representation
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
            # Track ID directly as string to preserve structure mapping consistency
            y.append(str(student.get('student_id')))

    if len(X) == 0:
        return None
    
    # Needs at least 2 categories to fit classifier correctly, otherwise return basic structural map
    distinct_classes = len(set(y))
    if distinct_classes >= 2:
        clf = SVC(kernel='linear', probability=True, class_weight='balanced')
        try:
            clf.fit(X, y)
            return {'clf': clf, 'X': X, "y": y, "multi_class": True}
        except ValueError:
            return {'X': X, "y": y, "multi_class": False}
            
    return {'X': X, "y": y, "multi_class": False}

def train_classifier():
    st.cache_resource.clear()
    model_data = get_trained_model()
    return bool(model_data)

def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)
    detected_student = {}
    model_data = get_trained_model()

    if not model_data or not encodings:
        return detected_student, [], len(encodings)
    
    X_train = model_data['X']
    y_train = model_data['y']
    multi_class = model_data.get('multi_class', False)
    all_students = sorted(list(set(y_train)))

    for encoding in encodings:
        if multi_class and 'clf' in model_data:
            predicted_id = str(model_data['clf'].predict([encoding])[0])
        else:
            # Distance-fallback algorithm for single-student verification contexts
            distances = [np.linalg.norm(np.array(emp) - encoding) for emp in X_train]
            min_index = np.argmin(distances)
            predicted_id = str(y_train[min_index])

        # Safely find index location mapping
        try:
            match_index = y_train.index(predicted_id)
            student_embedding = X_train[match_index]
            best_match_score = np.linalg.norm(student_embedding - encoding)
            
            resemblance_threshold = 0.6
            if best_match_score <= resemblance_threshold:
                detected_student[predicted_id] = True
        except ValueError:
            continue

    return detected_student, all_students, len(encodings)