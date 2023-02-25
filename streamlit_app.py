import streamlit as st
from PIL import Image

st.title("WELCOME")
image = Image.open('Image.jpg')
profile_pic = Image.open("Profile_pic.jpg")
st.image(image, caption = '')
st.header("About Us")
st.text("this web application was developed by....")
st.image(profile_pic, width=100, use_column_width=None, clamp=False, channels="RGB", caption = "SANJIV.R")
