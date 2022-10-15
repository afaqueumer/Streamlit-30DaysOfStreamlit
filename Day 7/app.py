import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

st.header('st.write')

# Example 1 - display text and Markdown-formatted text
st.write('Hello, *World!* 👋')

# Example 2 - display other data formats such as numbers
st.write(1234)

# Example 3 - display DataFrames
df = pd.DataFrame({
     'first column': [1, 2, 3, 4, 5],
     'second column': [10, 20, 30, 40, 50],
     'third column': ['a', 'b', 'c', 'd', 'e']
     })
st.write(df)

# Example 4 -  pass in multiple arguments
st.write('Below is a DataFrame: 👇', df, 'Above is a dataframe: 👆')

# Example 5 - display plot by passing it to a variable
df2 = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write('Below is a Chart: 👇', c)