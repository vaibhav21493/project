import streamlit as st
from datetime import datetime
from utils import (
    user_exists, save_user, is_valid_username,
    is_valid_password, is_valid_email, indian_states_cities
)

def second_pg():
    st.title("New User Registration")

    new_username = st.text_input("New Username", placeholder="At least 3 letters")
    new_password = st.text_input("New Password", type="password", placeholder="At least 1 uppercase, 1 number & 1 special char")
    full_name = st.text_input("Full Name")
    father_name = st.text_input("Father's Name")
    dob = st.date_input("Date of Birth", max_value=datetime.today())
    email = st.text_input("Email (must end with @gmail.com)", placeholder="example@gmail.com")
    state = st.selectbox("State", sorted(indian_states_cities.keys()))
    city = st.selectbox("City", indian_states_cities[state])
    country = st.selectbox("Country", ["India"])

    if st.button("Register"):
        if not is_valid_username(new_username):
            st.error("Username must contain at least 3 letters (A-Z or a-z).")
        elif not is_valid_password(new_password):
            st.error("Password must contain at least one uppercase letter, one number, and one special character.")
        elif not is_valid_email(email):
            st.error("Email must be a valid Gmail address ending with '@gmail.com'.")
        elif user_exists(new_username):
            st.error("Username already exists. Please choose a different one.")
        else:
            user_data = {
                "username": new_username,
                "password": new_password,
                "full_name": full_name,
                "father_name": father_name,
                "dob": dob.strftime("%Y-%m-%d"),
                "email": email,
                "city": city,
                "state": state,
                "country": country
            }
            save_user(user_data)
            st.success("Registration successful! Please log in.")
            st.rerun()

