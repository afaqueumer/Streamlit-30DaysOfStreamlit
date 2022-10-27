import streamlit as st
import pandas as pd

st.title('st.file_uploader 📂')

st.subheader('CSV Upload')
uploaded_file = st.file_uploader("Choose a csv file", type = ['.csv'])

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df.head(4))
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
  
st.subheader('Image Upload') 
uploaded_img = st.file_uploader("Choose an image", type = ['.jpg', '.png'])
if uploaded_img is not None:
  st.image(uploaded_img, width = 720)
else:
  st.info('☝️ Upload an image file')