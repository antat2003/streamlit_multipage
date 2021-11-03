import streamlit as st
from streamlit.components.v1 import components
from streamlit.report_thread import get_report_ctx
from util.session import *
from pages import login, about, register

_custom_slider = components.declare_component(
    "custom_slider",
    url='http://localhost:3000'
)

def custom_slider(options, key=None):
    return _custom_slider(options=options, key=key, default=0)

def app():
    
    if not login_status():
        genre = st.radio("What do you want to do?", ('Login', 'Register'))
        if genre == 'Login':
            login.app(about)
        else:
            register.app(about)

    else:
        st.markdown("## About Page")
        ctx = get_report_ctx()
        print(ctx.session_id)
        
        st.write("You login: ", login_status())
        logout_buttton = st.sidebar.button('Logout')
        if logout_buttton:
            logout()
            st.experimental_rerun()



    