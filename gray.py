import streamlit as st
from PIL import Image

st.subheader("Colour Image to Grayscale Converter") 

uploaded_img = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")


if camera_image:
    # Create pillow img instance
    img = Image.open(camera_image)
    
    # Convert img to grayscale 
    gray_img = img.convert("L")

    # Render the Grayscale img 
    st.image(gray_img)

if uploaded_img:
    img = Image.open(uploaded_img)
    gray_uploaded_img = img.convert("L")
    st.image(gray_uploaded_img)