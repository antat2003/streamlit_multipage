import streamlit as st
from streamlit.components.v1 import components
from streamlit.report_thread import get_report_ctx
from util.session import *
from multipage import MultiPage
from pages import about, register

def app(page):
    title_container = st.empty()
    email_input_container = st.empty()
    pw_input_container = st.empty()
    login_button_container = st.empty()

    # title_container.write("Login")
    email = email_input_container.text_input("Email")
    password = pw_input_container.text_input("Password", type="password")
    login_button = login_button_container.button('Login')

    if login_button:
        title_container.empty()
        email_input_container.empty()
        pw_input_container.empty()
        login_button_container.empty()
        login()
        page.app()
        st.experimental_rerun()