import streamlit as st
from supabase import Client,create_client

supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]   # yeah supabse  ka projecct and key ko acces kar rhe h aur jo ki secrets.toml file me h 
)
