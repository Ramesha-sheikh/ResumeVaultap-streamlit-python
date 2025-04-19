import streamlit as st

# Function to get user input for resume data and passkey
def get_user_input():
    resume_data = st.text_area("Enter your Resume Data:")
    passkey = st.text_input("Enter passkey:", type="password")
    return resume_data, passkey
