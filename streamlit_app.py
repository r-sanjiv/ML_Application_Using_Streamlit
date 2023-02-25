import streamlit as st
from PIL import Image

st.title("ARTIFICIAL INTELLIGENCE")
image = Image.open('Image.jpg')
st.header("WHAT IS AI ?")
st.markdown("Artificial intelligence (AI) involves using computers to do things that traditionally require human intelligence")
st.image(Image.open("Image.jpg"))
st.header("Types fo Artificial Intelligence (AI),\n Artificial General Intelligence (AGI),\n Artificial Super Intelligence (ASI)")
st.text("Artificial Narrow Intelligence (ANI)")
st.text("Artificial General Intelligence (AGI)")
st.text("Artificial Super Intelligence (ASI)")
profile_pic = Image.open("Profile_pic.jpg")
st.image(image, caption = '')
st.header("About Us")
st.image(profile_pic, width=100, use_column_width=None, clamp=False, channels="RGB", caption = "SANJIV.R")
st.markdown("AI Engineer and Quantam Meachine Learning Engineer")
