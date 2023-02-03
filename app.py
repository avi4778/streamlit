# python -m streamlit run app.py

import streamlit as st
from datetime import time
import datetime
import pandas as pd

# Streamlit Header

st.header('StreamLit Experiment')

# Slider

age = st.slider('How old are you?', min_value = 1, max_value = 70,
                 value = 26)
st.write("I'm ", age, 'years old')

values = st.slider(
    'Range Slider',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Start Day Four Complete video of streamlit by Ken Jee

# Markdown

st.write('Hello, **World!** :sunglasses:')

# DataFrame

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

import streamlit as st

# Code and Latex

code1 = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code1, language='python')

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# Metric

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", value = "70 °F", delta = "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# Day 8

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

d = st.date_input(
"When\'s your birthday",
min_value = datetime.date(1960, 1, 1),
max_value = datetime.date(2024, 1, 1)
)