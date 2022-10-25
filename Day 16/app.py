import streamlit as st

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#AEFF00"
backgroundColor="#FFDD06"
secondaryBackgroundColor="#32A997"
textColor="#020202"
font="serif"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)