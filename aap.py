import streamlit as st
from predik import show_predik
from xplor import show_xplor


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predik()
else:
    show_xplor()
