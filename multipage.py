import streamlit as st
import streamlit.components.v1 as components
from pages import home

class MultiPage:

    def __init__(self) -> None:
        self.pages = []

    def add_page(self, title, func) -> None:

        """
        Args:
            title ([str]): Page title
            func: Python function to render
        """

        self.pages.append({
            "title": title,
            "function": func,
            "current": False
        })

    def run(self):
        default = True
        st.sidebar.markdown("App Navigation")
        
        nav_button = st.markdown(""" <style> div.stButton > button:first-child { border:none; background:none; } </style>""", unsafe_allow_html=True) 
        nav_button = st.markdown(""" <style> .css-1g71wml:focus:not(:active) { border-color: rgb(0, 0, 0); color: #602ff1; } </style>""", unsafe_allow_html=True) 
        nav_button = st.markdown(""" <style> .css-1g71wml:focus { box-shadow: none; border-color: rgb(0, 0, 0); } </style>""", unsafe_allow_html=True) 
        nav_button = st.markdown(""" <style> .css-1g71wml:hover { box-shadow: rgb(0, 0, 0); color: rgb(0, 0, 0); outline:none; } </style>""", unsafe_allow_html=True) 
            
        for page in self.pages:
            
            if st.sidebar.button(page['title']):
                page['function']()
                default = False
        
        if default:
            home.app()

        

