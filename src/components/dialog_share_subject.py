import streamlit as st
import segno
import io


@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    # FIXED: Added https:// and corrected the domain spelling to match your live 'mainn' app link
    app_domain = "https://snapclass-mainn.streamlit.app"
    join_url = f"{app_domain}/?join-code={subject_code}"

    st.header(f"Share {subject_name}")

    # Generate the QR matrix using the fully certified web link
    qr = segno.make(join_url)
    out = io.BytesIO()
    qr.save(out, kind='png', scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('### Copy Link')
        # This makes it easy for teachers to copy with one click
        st.code(join_url, language="text")
        st.caption("Subject Code:")
        st.code(subject_code, language="text")
        st.info('Copy this link to share on WhatsApp or Email.')

    with col2:
        st.markdown('### Scan to Join')
        # FIXED: Removed trailing whitespace and rendered via container width standards
        st.image(out.getvalue(), use_container_width=True, caption=f'Scan to join {subject_code}')