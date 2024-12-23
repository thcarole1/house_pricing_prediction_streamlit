# Import libraries
import streamlit as st

# Load custom CSS
with open("app/css/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
    """
    <h1>House price prediction </h1>
    <h2> Data inputs </h2>
    """,
    unsafe_allow_html=True
)
