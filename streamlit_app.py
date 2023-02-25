import streamlit as st
from PIL import Image

st.text("WELCOME")
image = Image.open('Image.jpg')
st.image(image, caption='')
