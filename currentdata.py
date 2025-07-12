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

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Select Appointment", "Enter Health Data", "Book Appointment"])

    if page == "Select Appointment":
        select_appointment_page()
    elif page == "Enter Health Data":
        health_data_page()
    elif page == "Book Appointment":
        book_appointment_page()

def select_appointment_page():
    st.title("Select Appointment")

    hospital_names = list(hospitals.keys())
    selected_hospital = st.selectbox("Select Hospital", hospital_names)
    st.session_state.selected_hospital = selected_hospital

    departments = list(hospitals[selected_hospital].keys())
    selected_department = st.selectbox("Select Department", departments)
    st.session_state.selected_department = selected_department

    doctors = hospitals[selected_hospital][selected_department]
    doctor_labels = [f"{doc['name']} (⭐ {doc['rating']}) - {doc['qualification']} - {doc['experience']}" for doc in doctors]
    selected_doctor_label = st.selectbox("Select Doctor", doctor_labels)
    doc_index = doctor_labels.index(selected_doctor_label)
    selected_doctor = doctors[doc_index]
    st.session_state.selected_doctor = selected_doctor

    appointment_date = st.date_input("Appointment Date", datetime.today())
    appointment_time = st.time_input("Appointment Time", datetime.now().time())
    st.session_state.appointment_date = str(appointment_date)
    st.session_state.appointment_time = str(appointment_time)

    if st.button("Save Appointment Details"):
        data = load_json_file(USE_DATA_FILE)
        data['appointment'] = {
            "selected_hospital": selected_hospital,
            "selected_department": selected_department,
            "selected_doctor": selected_doctor,
            "appointment_date": str(appointment_date),
            "appointment_time": str(appointment_time)
        }
        save_json_file(USE_DATA_FILE, data)
        st.success("Appointment details saved! Now enter health data or go to Book Appointment.")

def health_data_page():
    st.title("Patient Health Data")
    data = load_json_file(USE_DATA_FILE)
    health_data = data.get('health', {})

    weight = st.number_input("Weight (kg)", min_value=0.0, value=float(health_data.get("weight", 70)))
    height = st.number_input("Height (cm)", min_value=0.0, value=float(health_data.get("height", 170)))
    symptoms = st.text_area("Symptoms", value=health_data.get("symptoms", ""))
    pre_meds = st.text_area("Pre-Medicine Taking", value=health_data.get("pre_meds", ""))
    bp = st.text_input("Blood Pressure (mmHg)", value=health_data.get("bp", "120/80"))

    if st.button("Save Health Data"):
        data['health'] = {
            "weight": weight,
            "height": height,
            "symptoms": symptoms,
            "pre_meds": pre_meds,
            "bp": bp,
            "record_date": datetime.today().strftime("%Y-%m-%d")
        }
        save_json_file(USE_DATA_FILE, data)
        st.success("Health data saved! You can now book your appointment.")

def book_appointment_page():
    st.title("Book Appointment & Summary")
    data = load_json_file(USE_DATA_FILE)
    appointment = data.get('appointment', {})
    health = data.get('health', {})

    st.markdown("""
    <style>
    .blurred-container {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 18px;
        padding: 28px;
        margin-bottom: 30px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.25);
        border: 1px solid rgba(255,255,255,0.3);
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="blurred-container">', unsafe_allow_html=True)
    st.markdown("### Appointment Details")
    st.markdown(f"""
- **Hospital:** {appointment.get('selected_hospital', 'Not selected')}
- **Department:** {appointment.get('selected_department', 'Not selected')}
- **Doctor:** {appointment.get('selected_doctor', {}).get('name', 'Not selected')}
- **Date:** {appointment.get('appointment_date', 'Not selected')}
- **Time:** {appointment.get('appointment_time', 'Not selected')}
    """)
    st.markdown("---")
    st.markdown("### Patient Health Data")
    if health:
        st.markdown(f"""
- **Record Date:** {health.get('record_date', '')}
- **Weight:** {health.get('weight', '')} kg
- **Height:** {health.get('height', '')} cm
- **Blood Pressure:** {health.get('bp', '')}
- **Symptoms:** {health.get('symptoms', '')}
- **Pre-Medicine:** {health.get('pre_meds', '')}
        """)
    else:
        st.info("No patient health data found.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.header("Print and Payment")
    st.markdown("""
        <button onclick="window.print()" style="background-color:#4e8cff;color:white;padding:10px 24px;border:none;border-radius:6px;font-size:16px;cursor:pointer;">
            Print Appointment Summary
        </button>
        """, unsafe_allow_html=True)
    payment_method = st.selectbox("Select Payment Method", ["UPI", "Credit Card", "Debit Card", "Net Banking", "Cash"])
    if st.button("Pay Now"):
        st.success(f"Payment via {payment_method} successful! ")

# This function can be imported elsewhere:
def currentsdatas():
    health_data_page()

if __name__ == "__main__":
    main()
