import streamlit as st
from PIL import Image

st.title("ARTIFICIAL INTELLIGENCE")


st.header("WHAT IS AI ?")
st.markdown("Artificial intelligence (AI) involves using computers to do things that traditionally require human intelligence")

st.image(Image.open("Image_1.jpg"))

st.header("Types fo Artificial Intelligence (AI)")
st.markdown(" - Artificial Narrow Intelligence (Narrow AI)")
st.markdown(" - Artificial General Intelligence (FEneral AI)")
st.markdown(" - Artificial Super Intelligence (Super AI)")

st.image(Image.open("Image_2.jpg"))

st.header("What Is Narrow AI ?")
st.markdown("Narrow AI is also known as weak AI. It is an application of artificial intelligence technologies to enable a high functioning system that replicates human intelligence for a dedicated purpose.")
st.subheader("Examplefor Narrow AI")
st.markdown(" - Image and facial recognition systems.")
st.markdown(" - Chatbots and conversational assistants.")
st.markdown(" - Self-driving vehicles.")
st.markdown(" - Predictive maintenance models.")

st.image(Image.open("Image_3.jpg"))

st.header("What is General AI ?")
st.markdown("General AI is the representation of generalized human cognitive abilities in software so that, faced with an unfamiliar task, the AGI system could find a solution.")
st.subheader("Example for General AI")
st.markdown(" - Creativity.")
st.markdown(" - Sensory perception.")
st.markdown(" - Fine motor skills.")
st.markdown(" - Natural language understanding.")
st.markdown(" - Navigation.")

st.image(Image.open("Image_4.jpg"))

st.header("What Is Super AI ?")
st.markdown("Super AI is a form of AI that is capable of surpassing human intelligence by manifesting cognitive skills and developing thinking skills of its own.")
st.subheader("Example for Super AI")
st.markdown(" - Development of large language models.")
st.markdown(" - Advancements in multimodal AI.")
st.markdown(" - AI-driven programming.")
st.markdown(" - Vertical integration of AI solutions.")
st.markdown(" - AI-generated inventions.")
st.image(Image.open("Image_5.jpg"))

profile_pic = Image.open("Profile_pic.jpg")
url1 = "https://github.com/r-sanjiv"
url2 = "https://www.linkedin.com/in/sanjiv-r/"
st.header("About Us")
st.image(profile_pic, width=100, use_column_width=None, clamp=False, channels="RGB", caption = "SANJIV.R")
st.markdown("AI Engineer, Quantam Meachine Learning Engineer, Data Analyst, ML Front End and Back End Developer")
st.markdown("Contact Us")
st.markdonw("GitHub : "%url1)
st.markdown("LinedIn : "%url2)

