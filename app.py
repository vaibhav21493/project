import streamlit as st
import landing
import main

if "page" not in st.session_state:
    st.session_state["page"] = "landing"

if st.session_state["page"] == "main":
    main.main_pg()
else:
    landing.landing_page()
