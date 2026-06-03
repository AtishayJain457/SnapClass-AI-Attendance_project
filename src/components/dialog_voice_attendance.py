import streamlit as st
from src.pipelines.voice_pipeline import process_bulk_audio
from src.database.config import supabase
import pandas as pd
from datetime import datetime

@st.dialog('Voice Attendance')
def voice_attendance_dialog(selected_subject_id):
    st.write('Record audio of students saying "I am present". Then AI will recognize the students.')

    # Capture browser audio input data stream
    audio_data = st.audio_input("Record classroom audio")

    # FIXED: Added a condition to check if audio data is present before allowing button submission
    if st.button('Analyze Audio', width='stretch', type='primary', disabled=audio_data is None):
        with st.spinner('Processing audio data...'):
            enrolled_res = supabase.table('subject_students').select("*, students(*)").eq('subject_id', selected_subject_id).execute()
            enrolled_students = enrolled_res.data

            if not enrolled_students:
                st.warning('No students enrolled in this course.')
                return
                
            candidates_dict = {
                s['students']['student_id']: s['students']['voice_embedding'] 
                for s in enrolled_students if s['students'].get('voice_embedding')
            }

            if not candidates_dict:
                st.error('No enrolled students have voice profiles registered.')
                return
            
            # FIXED: Safe to read now because button verification checks for NoneType objects
            audio_bytes = audio_data.read()

            detected_scores = process_bulk_audio(audio_bytes, candidates_dict)
            results, attendance_to_log = [], []
            current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

            for node in enrolled_students:
                student = node['students']
                score = detected_scores.get(student['student_id'], 0.0)
                is_present = bool(score > 0.5) # Assuming a 0.5 threshold for verification matches

                results.append({
                    "Name": student['name'],
                    "ID": student['student_id'],
                    "Match Score": f"{score:.2f}" if is_present else "-",
                    "Status": "✅ Present" if is_present else "❌ Absent"
                })

                attendance_to_log.append({
                    'student_id': student['student_id'],
                    'subject_id': selected_subject_id,
                    'timestamp': current_timestamp,
                    'is_present': bool(is_present)
                })
                
            st.session_state.voice_attendance_results = (pd.DataFrame(results), attendance_to_log)

    # --- RENDER RESULTS MATRIX DIRECTLY INSIDE MODAL WORKFLOW CONTAINER ---
    if st.session_state.get('voice_attendance_results'):
        st.divider()
        df_results, logs = st.session_state.voice_attendance_results
        
        st.subheader("Analysis Results")
        st.dataframe(df_results, use_container_width=True, hide_index=True)
        
        # Added a confirmation button layout inside the dialogue modal interface framework
        if st.button("Confirm and Log Attendance", type="secondary", width="stretch"):
            try:
                supabase.table('attendance_logs').insert(logs).execute()
                st.toast("Voice attendance saved successfully! 🎉")
                del st.session_state.voice_attendance_results
                import time
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Database sync failed: {str(e)}")