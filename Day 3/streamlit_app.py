import streamlit as st

st.header('st.button', anchor='st.button')

if st.button('Say hello'):
     st.write("Hello there 👋 (st.button = True)")
else:
     st.write("Goodbye !! (st.button = False) ")