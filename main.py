# # import streamlit as st
# # import base64
# # from home import first_pg
# # from register import second_pg

# # def set_background(image_url=None, local_file=None):
# #     """
# #     Sets a background image for the Streamlit app.
# #     - If image_url is provided, uses it as the background.
# #     - If local_file is provided, encodes and uses it as the background.
# #     """
# #     if image_url:
# #         st.markdown(
# #             f"""
# #             <style>
# #             .stApp {{
# #                 background-image: url("{image_url}");
# #                 background-attachment: fixed;
# #                 background-size: cover;
# #                 background-repeat: no-repeat;
# #             }}
# #             </style>
# #             """,
# #             unsafe_allow_html=True
# #         )
# #     elif local_file:
# #         with open(local_file, "rb") as img_file:
# #             encoded = base64.b64encode(img_file.read()).decode()
# #         # Guess MIME type from file extension
# #         ext = local_file.split('.')[-1].lower()
# #         mime = "png" if ext == "png" else "jpeg"
# #         st.markdown(
# #             f"""
# #             <style>
# #             .stApp {{
# #                 background-image: url("data:image/{mime};base64,{encoded}");
# #                 background-size: cover;
# #                 background-repeat: no-repeat;
# #                 background-attachment: fixed;
# #             }}
# #             </style>
# #             """,
# #             unsafe_allow_html=True
# #         )

# # # --- Set your background here ---
# # # To use a URL:
# # # set_background(image_url="https://your-image-url.com/image.jpg")
# # # To use a local file:
# import streamlit as st
# import base64
# import os
# from home import first_pg
# from register import second_pg

# def set_background(image_url=None, local_file=None):
#     # ... (same as above) ...

# def main_pg():
#     set_background(local_file=os.path.join("static", "images", "mainque.jpg"))
#     st.title("Queue Management System")
#     page = st.sidebar.radio('Choose action', ['Login', 'Register'])

#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False
#     if "current_user" not in st.session_state:
#         st.session_state.current_user = ""

#     if not st.session_state.logged_in:
#         if page == "Login":
#             first_pg()
#         elif page == "Register":
#             second_pg()
#     else:
#         st.title(f"Welcome, {st.session_state.current_user}!")
#         st.write("You are logged in.")
#         if st.button("Logout"):
#             st.session_state.logged_in = False
#             st.session_state.current_user = ""
#             st.experimental_rerun()

#     st.markdown("""
#         <style>
#         [data-testid="stSidebar"] {
#             background: #e0f2f1;
#             color: #222222;
#         }
#         [data-testid="stSidebar"] .css-1d391kg {
#             color: #00695c;
#         }
#         [data-testid="stSidebar"] label {
#             color: #00695c;
#             font-weight: bold;
#         }
#         </style>
#     """, unsafe_allow_html=True)
import streamlit as st
import base64
import os
from home import first_pg
from register import second_pg
from depertment import depertmentblog
from currentdata import currentsdatas
from bookappoint import bookappointpage  # Ensure this function exists in bookappoint.py

def set_background(local_file=None):
    if local_file:
        if not os.path.isfile(local_file):
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

def main_pg():
    # Use a raw string for the Windows path to avoid escape sequence issues
    set_background(local_file=r"C:\Users\VAIBHAV\Desktop\queueM\static\images\maingue4.png")

    st.title("Queue Management System")
    page = st.sidebar.radio('Choose action', ['Login', 'Register'])

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "current_user" not in st.session_state:
        st.session_state.current_user = ""

    if not st.session_state.logged_in:
        if page == "Login":
            first_pg()
        elif page == "Register":
            second_pg()
    else:
        st.title(f"Welcome, {st.session_state.current_user}!")
        st.write("You are logged in.")

        # Sidebar navigation for logged-in users
        logged_in_page = st.sidebar.radio(
            "Go to page:",
            ["Departments", "Patient Health Data", "Book Appointment"],
            key="logged_in_nav"
        )

        if logged_in_page == "Departments":
            depertmentblog()
        elif logged_in_page == "Patient Health Data":
            currentsdatas()
        elif logged_in_page == "Book Appointment":
            bookappointpage()

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.current_user = ""
            st.rerun()

    # Sidebar styling (optional)
    st.markdown("""
        <style>
        [data-testid="stSidebar"] {
            background: #e0f2f1;
            color: #222222;
        }
        [data-testid="stSidebar"] .css-1d391kg {
            color: #00695c;
        }
        [data-testid="stSidebar"] label {
            color: #00695c;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main_pg()
