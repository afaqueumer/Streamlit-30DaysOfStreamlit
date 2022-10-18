import streamlit as st

# header
st.header('st.selectbox')

# create a color dictionary
colors_dic = {"Red" : "🔴", "Blue" : "🔵" , "Green" : "🟢", "Yellow" : "🟡"}

# create a drop down
color = st.selectbox('What is your favourite color ? Select from the dropdown 👇', options = colors_dic.keys(), index=2)

#display the seleccted value
st.write('Your favourite color is  ➡️ ', colors_dic[color])