import streamlit as st 
import pandas as pd
import numpy as np
st.title("Hello Streamlit!")
st.write("Heyy there")

df = pd.DataFrame({'first column': [1, 2, 3], 'second column': [4, 5, 6]})
st.write('Here is the data frame:')
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.write(chart_data)

st.line_chart(chart_data)


name = st.text_input('Enter your name')

if name:
    st.write(name)

age = st.slider('Select your age', 0, 100, 25)
st.write(f'Your age is {age}')

options = ['Python', 'Java', 'C', 'C++', 'JavaScript']
choice = st.selectbox('Choose your favorite programming language', options)
st.write(choice)  

uploaded_file = st.file_uploader('Choose a CSV file', type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)      