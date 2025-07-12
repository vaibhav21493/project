import streamlit as st
import json
import os
from datetime import datetime

USERS_DATA_FILE = "users_data.json"

def load_json_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    data = {}
                return data
            except json.JSONDecodeError:
                return {}
    return {}

def bookappointpage():
    st.title("Book Appointment & Summary")

    # Safely get session state data with defaults
    selected_hospital = st.session_state.get('selected_hospital', "Not selected")
    selected_department = st.session_state.get('selected_department', "Not selected")
    selected_doctor = st.session_state.get('selected_doctor', {})
    appointment_date = st.session_state.get('appointment_date', datetime.today().strftime("%Y-%m-%d"))
    appointment_time = st.session_state.get('appointment_time', "09:00 AM")

    # Doctor name fallback
    doctor_name = "Not selected"
    if isinstance(selected_doctor, dict):
        doctor_name = selected_doctor.get('name', "Not selected")
    elif isinstance(selected_doctor, str):
        doctor_name = selected_doctor

    # Load latest health data
    user_data = load_json_file(USERS_DATA_FILE)
    if user_data:
        latest_date = sorted(user_data.keys(), reverse=True)[0]
        health_data = user_data[latest_date]
    else:
        latest_date = None
        health_data = {}

    # CSS for blurred background container
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
        max-width: 650px;
        margin-left: auto;
        margin-right: auto;
    }
    .info-msg {
        color: #31708f;
        background-color: #d9edf7;
        border: 1px solid #bce8f1;
        border-radius: 6px;
        padding: 10px 16px;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Build HTML content for the blurred box
    details_html = f"""
    <div class="blurred-container">
      <h3>Appointment Details</h3>
      <ul>
        <li><b>Hospital:</b> {selected_hospital}</li>
        <li><b>Department:</b> {selected_department}</li>
        <li><b>Doctor:</b> {doctor_name}</li>
        <li><b>Date:</b> {appointment_date}</li>
        <li><b>Time:</b> {appointment_time}</li>
      </ul>
      <hr>
      <h3>Patient Health Data</h3>
    """

    if health_data:
        details_html += f"""
        <ul>
          <li><b>Record Date:</b> {latest_date}</li>
          <li><b>Weight:</b> {health_data.get('weight', '')} kg</li>
          <li><b>Height:</b> {health_data.get('height', '')} cm</li>
          <li><b>Blood Pressure:</b> {health_data.get('bp', '')}</li>
          <li><b>Symptoms:</b> {health_data.get('symptoms', '')}</li>
          <li><b>Pre-Medicine:</b> {health_data.get('pre_meds', '')}</li>
        </ul>
        """
    else:
        details_html += '<div class="info-msg">No patient health data found.</div>'

    details_html += "</div>"

    st.markdown(details_html, unsafe_allow_html=True)

    st.markdown("---")
    st.header("Print and Payment")

    # Print Button (browser print dialog)
    st.markdown("""
        <button onclick="window.print()" style="background-color:#4e8cff;color:white;padding:10px 24px;border:none;border-radius:6px;font-size:16px;cursor:pointer;">
            Print Appointment Summary
        </button>
        """, unsafe_allow_html=True)

    # Payment Option (Demo)
    payment_method = st.selectbox("Select Payment Method", ["UPI", "Credit Card", "Debit Card", "Net Banking", "Cash"])
    if st.button("Pay Now"):
        st.success(f"Payment via {payment_method} successful! (Demo)")

# THIS IS THE FUNCTION YOU MUST IMPORT:
# from bookappoint import bookappointpage

if __name__ == "__main__":
    bookappointpage()

