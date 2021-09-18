import streamlit as st

from multipage import MultiPage
from pages import about, eviction, stock, employ

app = MultiPage()

# st.title("Page Title")

#Add all your applications (pages) here

app.add_page("Employment data", employ.app)
app.add_page("Eviction data", eviction.app)
app.add_page("Stock Market", stock.app)
app.add_page("About", about.app)

app.run()
