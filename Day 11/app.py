import streamlit as st

st.header('st.multiselect')

superheroes = ["Batman", "Superman", "Spider Man", "The Flash", "Thor", "Captain America","Iron Man",  "Wonder Woman", "Wolverine"]

options = st.multiselect('Select your favourite Superheroes 🔥',  options = superheroes, default=["Batman", "Superman"])

st.write('Your Superhero list ⬇️', options)