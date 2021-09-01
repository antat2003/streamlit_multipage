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
        
        for page in self.pages:
            if st.sidebar.button(page['title']):
                page['function']()
                default = False
        
        if default:
            home.app()

        

