import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    st.set_page_config(
        page_title='SnapClass - Making Attendance faster using AI',
        page_icon="https://i.ibb.co/YTYGn5qV/logo.png"
    )
    
    # 1. Initialize global authentication states safely
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None
    if 'is_logged_in' not in st.session_state:
        st.session_state['is_logged_in'] = False

    # --- 2. INTERCEPT REDIRECTION ROUTING & PURGE URL LOOP IMMEDIATELY ---
    url_join_code = st.query_params.get('join-code')
    
    if url_join_code:
        # Cache code into secure session memory so camera updates can't wipe it out
        st.session_state['pending_join_code'] = url_join_code
        
        # FIXED: Wipe query params from the URL string to break the rerun loop cleanly
        if 'join-code' in st.query_params:
            del st.query_params['join-code']
        
        # Route execution view context directly to student mode
        st.session_state['login_type'] = 'student'
        st.rerun()

    # --- 3. PERSIST AUTO-ENROLL UNTIL FACIAL IDENTITY VALIDATION ---
    pending_code = st.session_state.get('pending_join_code')
    
    if pending_code:
        # If they are already verified/logged in as a student, drop down the auto-enroll modal!
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(pending_code)
            # Remove from memory after successful dropdown display to prevent loops
            del st.session_state['pending_join_code']
        else:
            # Renders an informative instruction banner directly above the camera tracker frame
            st.warning("🔒 Please complete your FaceID verification below to automatically complete enrollment into this course!")

    # --- 4. RENDER CORE GRAPHICAL GRAPH LAYOUTS ---
    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()
        
        case None:
            home_screen()

if __name__ == "__main__":
    main()