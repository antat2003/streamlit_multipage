import streamlit as st
from streamlit.components.v1 import components
from streamlit.report_thread import get_report_ctx
from util.session import *
from multipage import MultiPage
from pages import register

def app(page):
    if not login_status():
        title_container = st.empty()
        remail_input_container = st.empty()
        rpw_input_container = st.empty()
        rregister_button_container = st.empty()

        # title_container.write("Register")
        email = remail_input_container.text_input("Email ")
        password = rpw_input_container.text_input("Password ", type="password")
        rregister_button = rregister_button_container.button('Register')

        if rregister_button:
            title_container.empty()
            remail_input_container.empty()
            rpw_input_container.empty()
            rregister_button_container.empty()
            login()
            page.app()
            st.experimental_rerun()