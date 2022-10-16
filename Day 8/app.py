import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Example 1
st.subheader('Slider')
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Example 2
st.subheader('Range slider - (int)')
values = st.slider('Select a range of values', 0, 100, (25, 75))
st.write('Values:', values)

# Example 3
st.subheader('Range slider - (float)')
values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0), step=0.1)
st.write('Values:', values)

# Example 4
st.subheader('Range time slider')
appointment = st.slider("Schedule your appointment:", value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 5
st.subheader('Datetime slider')
start_time = st.slider("When do you start?", value=datetime(2020, 1, 1, 9, 30), format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)