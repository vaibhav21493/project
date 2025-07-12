# import streamlit as st
# import base64
# import os

# def set_background(local_file=None):
#     if local_file:
#         if not os.path.exists(local_file):
#             st.error(f"Background image not found at {local_file}")
#             return
#         with open(local_file, "rb") as img_file:
#             encoded = base64.b64encode(img_file.read()).decode()
#         ext = local_file.split('.')[-1].lower()
#         mime = "png" if ext == "png" else "jpeg"
#         st.markdown(
#             f"""
#             <style>
#             .stApp {{
#                 background-image: url("data:image/{mime};base64,{encoded}");
#                 background-size: cover;
#                 background-repeat: no-repeat;
#                 background-attachment: fixed;
#             }}
#             </style>
#             """,
#             unsafe_allow_html=True,
#         )

# def landing_page():
#     # Use your absolute path for the background image
#     set_background(local_file=r"C:\Users\VAIBHAV\Desktop\queueM\static\images\maingue4.png")

#     st.markdown(
#         """
#         <div style="display:flex; flex-direction: column; justify-content: center; align-items: center; height: 80vh;">
#             <h1 style="color: black; text-shadow: 2px 2px 8px white;">Welcome to Queue Management System</h1>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

#     if st.button("Start"):
#         st.session_state["page"] = "main"
#         st.rerun()
import streamlit as st
import base64
import os

def set_background(local_file=None):
    if local_file:
        if not os.path.exists(local_file):
            st.error(f"Background image not found at {local_file}")
            return
        with open(local_file, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
        ext = local_file.split('.')[-1].lower()
        mime = "png" if ext == "png" else "jpeg"
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/{mime};base64,{encoded}");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-position: center;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )

def landing_page():
    set_background(local_file=r"C:\Users\VAIBHAV\Desktop\queueM\static\images\maingue4.png")

    st.markdown("""
        <style>
        .info-card {
            background: rgba(255,255,255,0.95);
            border-radius: 18px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.13);
            padding: 24px 20px;
            max-width: 280px;
            min-height: 220px;
            text-align: center;
            margin-bottom: 12px;
            transition: box-shadow 0.2s;
        }
        .info-card:hover {
            box-shadow: 0 12px 36px 0 rgba(31, 38, 135, 0.18);
        }
        .hospital-logo-img {
            width: 90px;
            height: 90px;
            object-fit: contain;
            border-radius: 16px;
            background: #fff;
            box-shadow: 0 2px 8px rgba(0,0,0,0.10);
            padding: 8px;
            margin-bottom: 10px;
        }
        .start-btn {
            background: linear-gradient(90deg,#4e8cff,#38d39f);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 16px 48px;
            font-size: 1.3rem;
            font-weight: bold;
            margin-top: 32px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.13);
            cursor: pointer;
            transition: background 0.2s;
        }
        .start-btn:hover {
            background: linear-gradient(90deg,#38d39f,#4e8cff);
        }
        .logo-row {
            display: flex;
            justify-content: center;
            gap: 48px;
            margin-top: 20px;
            margin-bottom: 40px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Centered welcome message
    st.markdown(
        """
        <div style="display:flex; flex-direction: column; align-items: center; margin-top: 40px;">
            <h1 style="color: #22223b; margin-bottom: 12px; text-shadow: 2px 2px 8px #fff;">
                👋 Welcome to <span style="color:#4e8cff;">Queue Management System</span>
            </h1>
            <p style="color:#22223b; font-size:1.1rem; margin-bottom: 0;">
                Efficiently manage patient queues, reduce wait times, and enhance hospital experiences.<br>
                <b>Explore our features below!</b>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- Logos at the top in a row ---
    st.markdown("""
        <div class="logo-row">
            <img src="https://cdn-icons-png.flaticon.com/512/2965/2965567.png" class="hospital-logo-img" alt="City Hospital Logo" title="City Hospital">
            <img src="https://cdn-icons-png.flaticon.com/512/2965/2965568.png" class="hospital-logo-img" alt="Green Valley Clinic Logo" title="Green Valley Clinic">
            <img src="https://cdn-icons-png.flaticon.com/512/2965/2965569.png" class="hospital-logo-img" alt="Sunrise Hospital Logo" title="Sunrise Hospital">
        </div>
    """, unsafe_allow_html=True)

    # --- Informational Cards in a row with smaller width ---
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.markdown("""
            <div class="info-card">
                <h3>⏳ Live Queue Tracking</h3>
                <p>Monitor real-time patient flow and waiting times for every department, improving transparency and efficiency.</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="info-card">
                <h3>📱 Online Appointment Booking</h3>
                <p>Patients can book, reschedule, or cancel appointments online, reducing overcrowding and saving time.</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="info-card">
                <h3>📊 Analytics Dashboard</h3>
                <p>Gain insights into patient volumes, peak hours, and service bottlenecks to optimize hospital resources.</p>
            </div>
        """, unsafe_allow_html=True)

    # --- Start Button Centered ---
    st.markdown("<div style='display:flex; justify-content:center;'>", unsafe_allow_html=True)
    if st.button("Start", key="start_btn"):
        st.session_state["page"] = "main"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    landing_page()
