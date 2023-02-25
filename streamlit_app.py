import streamlit as st
from PIL import Image

st.title("ARTIFICIAL INTELLIGENCE")
image = Image.open('Image.jpg')
st.header("what is AI ?..")
st.markdown("Artificial intelligence (AI) involves using computers to do things that traditionally require human intelligence")
st.subheader("Types fo Artificial Intelligence (AI)")
st.markdown("Artificial Narrow Intelligence (ANI)")
st.markdown("Artificial General Intelligence (AGI)")
st.markdown("Artificial Super Intelligence (ASI)")
profile_pic = Image.open("Profile_pic.jpg")
st.image(image, caption = '')
st.header("About Us")
st.image(profile_pic, width=100, use_column_width=None, clamp=False, channels="RGB", caption = "SANJIV.R")
st.markdown("AI Engineer and Quantam Meachine Learning Engineer")
