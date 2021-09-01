import streamlit as st

from multipage import MultiPage
from pages import about, hello, home

app = MultiPage()

# st.title("Page Title")

#Add all your applications (pages) here

app.add_page("Home", home.app)
app.add_page("Hello", hello.app)
app.add_page("About", about.app)

app.run()
