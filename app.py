import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    st.set_page_config(
        page_title='SnapClass - Making Attendance Faster using AI',
        page_icon="https://i.ibb.co/YTYGn5qV/logo.png"
    )
    # 1. Initialize global session states if they don't exist
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None
    if 'is_logged_in' not in st.session_state:
        st.session_state['is_logged_in'] = False

    # --- 2. HANDLE URL AUTO-ENROLLMENT INTERCEPTION FIRST ---
    join_code = st.query_params.get('join-code')
    
    if join_code:
        # Force the view state to student mode immediately so they are on the right page
        if st.session_state['login_type'] != 'student':
            st.session_state['login_type'] = 'student'
            st.rerun()
            
        # If they are already verified/logged in as a student, open the modal over their dashboard
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)
        else:
            # If not logged in yet, gently warn them on the camera screen
            st.warning("Please verify your FaceID to complete automatic enrollment into this course!")

    # --- 3. RENDER THE CONTENT VIEW BASED ON STATE ---
    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()
        
        case None:
            home_screen()

if __name__ == "__main__":
    main()