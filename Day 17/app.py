import streamlit as st

st.title('st.secrets')

st.write("These are secret credentials")
st.write(st.secrets['name'])
st.write(st.secrets['password'])