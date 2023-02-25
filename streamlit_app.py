import streamlit as st
from PIL import Image

st.text("WELCOME")
image = Image.open('https://github.com/r-sanjiv/ML_Application_Using_Streamlit/blob/1db6ffd3cec5d28b406be9dbb70d93ff8c85ea9f/Image.jpg')
st.image(image, caption='')
