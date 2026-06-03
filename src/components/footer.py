import streamlit as st


def footer_home():
    # Tailored for your home landing screen with white contrast text
    st.markdown("""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
        <p style="font-weight:bold; color:white; margin:0;"> Created with ❤️ by <span style="color:#EB459E;">Atishay Jain</span></p>  
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    # Tailored for your student and teacher dashboards with black contrast text
    st.markdown("""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
        <p style="font-weight:bold; color:black; margin:0;"> Created with ❤️ by <span style="color:#5865F2;">Atishay Jain</span></p>  
        </div>
                
                """, unsafe_allow_html=True)