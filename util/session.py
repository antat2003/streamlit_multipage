import streamlit as st

def login_status() -> bool:
    if 'login' not in st.session_state:
	    return False
    return st.session_state.login

def login():
    st.session_state.login = True
    return 

def logout():
    st.session_state.login = False
    return
