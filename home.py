import streamlit as st
from utils import (
    user_exists, check_credentials, is_valid_username,
    is_valid_password, generate_captcha
)

def first_pg():
    st.title("Existing User Login")

    username = st.text_input("Username", placeholder="At least 3 letters")
    password = st.text_input("Password", type="password", placeholder="At least 1 uppercase, 1 number & 1 special char")

    if "captcha" not in st.session_state:
        st.session_state.captcha = generate_captcha()
    if st.button("Refresh Captcha"):
        st.session_state.captcha = generate_captcha()

    st.write("Enter the captcha below:")
    st.code(st.session_state.captcha, language='markdown')
    captcha_input = st.text_input("Captcha")

    if st.button("Login"):
        if not is_valid_username(username):
            st.error("Username must contain at least 3 letters (A-Z or a-z).")
        elif not is_valid_password(password):
            st.error("Password must contain at least one uppercase letter, one number, and one special character.")
        elif not user_exists(username):
            st.error("User does not exist. Please register first.")
        elif not check_credentials(username, password):
            st.error("Incorrect password.")
        elif captcha_input.strip().upper() != st.session_state.captcha:
            st.error("Incorrect captcha. Please try again.")
            st.session_state.captcha = generate_captcha()  # refresh captcha on failure
        else:
            st.session_state.logged_in = True
            st.session_state.current_user = username
            st.success("Login successful!")
            del st.session_state.captcha
            st.rerun()

