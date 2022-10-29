import streamlit as st
import time
     
with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

st.subheader("Timer ⌛️")
timer = st.number_input('Select number of Seconds 👇', min_value=1, max_value=100)
st.write(f'The current timer is set to 👉  {timer} seconds')

my_bar = st.progress(0)
frac = int((1/timer)*100)
prog = 0
for sec in range(1,timer+1):
     time.sleep(1)
     st.write(sec)
     prog+=frac
     my_bar.progress(prog)

st.snow()