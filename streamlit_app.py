import streamlit as st
from PIL import Image

st.text("WELCOME")
image = Image.open('https://github.com/r-sanjiv/ML_Application_Using_Streamlit/blob/main/Image.jpg?raw=true')
st.image(image, caption='')
