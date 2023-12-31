import streamlit as st
from PIL import Image
import os
from key import API_KEY
from google import generativeai as genai




st.markdown("<h1 style='text-align: center;'>Image Insight</h1>", unsafe_allow_html=True)
styled_text = "<h2 style='text-align: center; font-size: 20px;'>Extracting Meaningful Text from Pictures</h2>"
st.markdown(styled_text, unsafe_allow_html=True)



def get_api_key():
    text = st.sidebar.text_input("Enter API_key")
    return text

def model(img): 
    genai.configure(api_key =API_KEY )
    model = genai.GenerativeModel("gemini-pro-vision")
    response =  model.generate_content(img)
    return response.text




file = st.file_uploader("Upload image",type=["jpg","png","jpeg"])

if file is not None:
    img = Image.open(file)
    width, height = img.size
    new_width = 200  # Replace with the desired width
    new_height = int((new_width / width) * height)
    resized_img = img.resize((new_width, new_height))
    st.image(resized_img)
    button = st.button("Get Information")
    if button:
        text = model(img)
        st.write(text)


st.markdown("<p style='position: fixed; bottom: 15px; width: 100%;font-size: 12px;'>All Rights Reserved © 2023 at Lalit Mahale</p>", unsafe_allow_html=True)
