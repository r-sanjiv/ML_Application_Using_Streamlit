import streamlit as st
from PIL import Image

st.title("ARTIFICIAL INTELLIGENCE")
image = Image.open('Image.jpg')
st.header("WHAT IS AI ?")
st.markdown("Artificial intelligence (AI) involves using computers to do things that traditionally require human intelligence")
st.image(Image.open("Image.jpg"))
st.header("Types fo Artificial Intelligence (AI)")
st.text("Artificial Narrow Intelligence (Narrow AI)\nArtificial General Intelligence (FEneral AI)\nArtificial Super Intelligence (Super AI)")
st.header("What Is Narrow AI ?")
st.text("Narrow AI is also known as weak AI\nIt is an application of artificial intelligence technologies to enable a high functioning system that replicates human intelligence for a dedicated purpose.\nExample for Narrow AI\nImage and facial recognition systems\nChatbots and conversational assistants\nSelf-driving vehicles\nPredictive maintenance models")
st.header("What is General AI ?")
st.text("Artificial general intelligence (AGI) is the representation of generalized human cognitive abilities in software so that, faced with an unfamiliar task, the AGI system could find a solution.\nExample for General AI\nCreativity\nSensory perception\nFine motor skills\nNatural language understanding\nNavigation")
st.header("What Is Super AI ?")
st.text("Artificial superintelligence (ASI) is a form of AI that is capable of surpassing human intelligence by manifesting cognitive skills and developing thinking skills of its own.\nExample\nDevelopment of large language models\nAdvancements in multimodal AI\nAI-driven programming\nVertical integration of AI solutions\nAI-generated inventions")

profile_pic = Image.open("Profile_pic.jpg")
st.image(image, caption = '')
st.header("About Us")
st.image(profile_pic, width=100, use_column_width=None, clamp=False, channels="RGB", caption = "SANJIV.R")
st.markdown("AI Engineer and Quantam Meachine Learning Engineer")
