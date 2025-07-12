import streamlit as st
import json
import os
from datetime import datetime

USE_DATA_FILE = "use_data.json"  # Updated filename

def load_json_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_json_file(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

# Sample hospital data
hospitals = {
    "City Hospital": {
        "Cardiology": [
            {"name": "Dr. A. Sharma", "rating": 4.8, "qualification": "MD, DM (Cardiology)", "experience": "15 years"},
            {"name": "Dr. B. Verma", "rating": 4.6, "qualification": "MD, DNB (Cardiology)", "experience": "10 years"},
        ],
        "Neurology": [
            {"name": "Dr. C. Mehta", "rating": 4.7, "qualification": "MD, DM (Neurology)", "experience": "12 years"},
            {"name": "Dr. D. Nair", "rating": 4.5, "qualification": "MD, DNB (Neurology)", "experience": "9 years"},
        ],
    },
    "Green Valley Clinic": {
        "Orthopedics": [
            {"name": "Dr. E. Singh", "rating": 4.9, "qualification": "MS (Ortho), DNB (Ortho)", "experience": "18 years"},
            {"name": "Dr. F. Gupta", "rating": 4.6, "qualification": "MS (Ortho)", "experience": "11 years"},
        ],
        "Dermatology": [
            {"name": "Dr. O. Roy", "rating": 4.8, "qualification": "MD (Dermatology)", "experience": "11 years"},
            {"name": "Dr. P. Shah", "rating": 4.5, "qualification": "DDVL, MD (Dermatology)", "experience": "7 years"},
        ],
    }
}

def depertmentblog():
    st.title("Select Appointment")

    hospital_names = list(hospitals.keys())
    selected_hospital = st.selectbox("Select Hospital", hospital_names)
    st.session_state.selected_hospital = selected_hospital

    departments = list(hospitals[selected_hospital].keys())
    selected_department = st.selectbox("Select Department", departments)
    st.session_state.selected_department = selected_department

    doctors = hospitals[selected_hospital][selected_department]
    doctor_labels = [
        f"{doc['name']} (⭐ {doc['rating']}) - {doc['qualification']} - {doc['experience']}"
        for doc in doctors
    ]
    selected_doctor_label = st.selectbox("Select Doctor", doctor_labels)
    doc_index = doctor_labels.index(selected_doctor_label)
    selected_doctor = doctors[doc_index]
    st.session_state.selected_doctor = selected_doctor

    if st.button("Save Selection"):
        data = load_json_file(USE_DATA_FILE)
        data['appointment'] = {
            "selected_hospital": selected_hospital,
            "selected_department": selected_department,
            "selected_doctor": selected_doctor
        }
        save_json_file(USE_DATA_FILE, data)
        st.success("Selection saved!")

if __name__ == "__main__":
    depertmentblog()
