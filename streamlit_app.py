import streamlit as st
from PIL import Image

st.text("WELCOME")
image = Image.open('Image.jpg')
profile_pic = Image.open("Profile_pic.jpg")
st.image(image, caption = '')
set_page_config(layout = "wide")
Header.text("About Us")
st.text("this web application was developed by...................")
st.image(profile_pic, caption = "SANJIV.R")
