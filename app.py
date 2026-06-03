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
    
    # 1. Initialize global states safely
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None
    if 'is_logged_in' not in st.session_state:
        st.session_state['is_logged_in'] = False

    # --- 2. INTERCEPT LINK AND CLEAR URL LOOP IMMEDIATELY ---
    url_join_code = st.query_params.get('join-code')
    
    if url_join_code:
        # Save code into session memory where camera refreshes can't delete it
        st.session_state['pending_join_code'] = url_join_code
        
        # Wipe the query params from the URL bar to break the rerun loop cleanly
        st.query_params.clear()
        
        # Route view context to student mode and rerun to render the camera frame
        st.session_state['login_type'] = 'student'
        st.rerun()

    # --- 3. PERSIST ENROLLMENT DIALOG UNTIL FACE VERIFICATION LOGS IN ---
    pending_code = st.session_state.get('pending_join_code')
    
    if pending_code:
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(pending_code)
            # Remove from memory after successful dropdown display
            del st.session_state['pending_join_code']
        else:
            # Displays cleanly over the face-scanning module layout
            st.warning("🔒 Please complete your FaceID verification below to automatically enroll in your course!")

    # --- 4. RENDER GRAPHICAL PANELS BASELINE ---
    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()
        
        case None:
            home_screen()

if __name__ == "__main__":
    main()