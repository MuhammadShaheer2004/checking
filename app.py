import streamlit as st
import requests
from PIL import Image
import numpy as np

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
headers = {"Hugging_Face": "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"}

def query_image_caption(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

# Title of the app
st.title("Image Captioning")

# Image upload
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Save the uploaded image temporarily
    temp_file_path = "temp_image.jpg"
    image.save(temp_file_path)

    # Generate caption using the Hugging Face API
    output = query_image_caption(temp_file_path)
    
    # Display the caption
    if 'caption' in output:
        st.write("Generated Caption:", output['caption'])
    else:
        st.write("Error in generating caption:", output)

    # User question input
    user_question = st.text_input("Ask a question about the image:")

    if user_question:
        st.write("You asked:", user_question)
        # Implement basic question handling
        if "who has the ball" in user_question.lower():
            st.write("I can provide a caption, but I cannot determine who has the ball without object detection.")
        else:
            st.write("I'm not sure how to answer that.")
