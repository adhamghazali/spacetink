
import streamlit as st

st.title("Automatic Character Creation")
st.markdown('choose type of characeter')


option = st.selectbox("",('Human', 'Robot', 'Vehicle' , 'Animal'))

text=st.text_input('describe your Character: ')

clicked=st.button('Generate 3D model')

if clicked: 
    video_file = open('./images/donkey_final_crop.mp4', 'rb')
    data = video_file.read()
    st.video(data, format="video/mp4", start_time=0)

