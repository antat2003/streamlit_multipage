import streamlit as st

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
            "function": func
        })

    def run(self):
        app = st.sidebar.selectbox(
            'App Navigation',
            self.pages,
            format_func=lambda app: app['title'])

        app['function']()

        

