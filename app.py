"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st


st.title("Automatic Character Creation")
st.markdown('choose type of characeter')


option = st.selectbox("",('Human', 'Robot', 'Vehicle' , 'Animal'))

