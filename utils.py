import os
import json
import streamlit as st
import pandas as pd
import re
import random
import string
import base64

USER_DATA_FILE = "user_data.json"

indian_states_cities = {
    "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Guntur"],
    "Arunachal Pradesh": ["Itanagar", "Tawang", "Pasighat"],
    "Assam": ["Guwahati", "Silchar", "Dibrugarh"],
    "Bihar": ["Patna", "Gaya", "Bhagalpur"],
    "Chhattisgarh": ["Raipur", "Bhilai", "Bilaspur"],
    "Goa": ["Panaji", "Margao", "Vasco da Gama"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara"],
    "Haryana": ["Gurgaon", "Faridabad", "Panipat"],
    "Himachal Pradesh": ["Shimla", "Manali", "Dharamshala"],
    "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad"],
    "Karnataka": ["Bengaluru", "Mysuru", "Mangalore"],
    "Kerala": ["Thiruvananthapuram", "Kochi", "Kozhikode"],
    "Madhya Pradesh": ["Bhopal", "Indore", "Gwalior"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
    "Manipur": ["Imphal", "Thoubal", "Bishnupur"],
    "Meghalaya": ["Shillong", "Tura", "Jowai"],
    "Mizoram": ["Aizawl", "Lunglei", "Champhai"],
    "Nagaland": ["Kohima", "Dimapur", "Mokokchung"],
    "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela"],
    "Punjab": ["Ludhiana", "Amritsar", "Jalandhar"],
    "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur"],
    "Sikkim": ["Gangtok", "Namchi", "Geyzing"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
    "Telangana": ["Hyderabad", "Warangal", "Nizamabad"],
    "Tripura": ["Agartala", "Udaipur", "Dharmanagar"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi"],
    "Uttarakhand": ["Dehradun", "Haridwar", "Nainital"],
    "West Bengal": ["Kolkata", "Howrah", "Durgapur"],
    "Delhi": ["New Delhi", "Dwarka", "Rohini"],
    "Jammu and Kashmir": ["Srinagar", "Jammu", "Anantnag"],
    "Ladakh": ["Leh", "Kargil"]
}

def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            try:
                users = json.load(f)
                if not isinstance(users, list):
                    users = []
            except json.JSONDecodeError:
                users = []
    else:
        users = []
    return pd.DataFrame(users)

def save_user(user_data):
    users = load_users()
    users_list = users.to_dict(orient="records") if not users.empty else []
    users_list.append(user_data)
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users_list, f, indent=4)

def user_exists(username):
    users = load_users()
    return username in users["username"].values if not users.empty else False

def check_credentials(username, password):
    users = load_users()
    if users.empty:
        return False
    return ((users["username"] == username) & (users["password"] == password)).any()

def is_valid_username(username):
    return len(re.findall(r'[A-Za-z]', username)) >= 3

def is_valid_password(password):
    has_upper = re.search(r'[A-Z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    return bool(has_upper and has_digit and has_special)

def is_valid_email(email):
    pattern = r'^[\w\.-]+@gmail\.com$'
    return re.match(pattern, email) is not None

def generate_captcha(length=5):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

def set_background(image_file):
    if not os.path.isfile(image_file):
        st.error(f"Background image '{image_file}' not found in {os.getcwd()}.")
        return
    ext = image_file.split('.')[-1]
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/{ext};base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
