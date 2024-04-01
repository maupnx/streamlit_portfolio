import streamlit as st
import pandas as pd
from PIL import Image
import os
import requests

def display_image(url_or_path, width=100):
    try:
        if os.path.exists(url_or_path):  # Check if the path exists locally
            image = Image.open(url_or_path)
        else:
            response = requests.get(url_or_path)
            image = Image.open(BytesIO(response.content))
        st.image(image, width=width)
    except Exception as e:
        st.error(f"Error loading image from {url_or_path}: {e}")


# Define the data
academic_data = {
    "Brand": ["Universidade de São Paulo (USP)", "FIAP"],
    "Logo": ["C:/Users/maula/OneDrive/Desktop/webpage/pages/images/usp2.jpg",
             "C:/Users/maula/OneDrive/Desktop/webpage/pages/images/fiap.png"],
    "Description": ["Bachelor Degree in MARKETING", "Master Business Administration in BIG DATA & DATA SCIENCE"]}

with st.expander("Academic"):
    # Display the data in a table
    for i in range(len(academic_data["Description"])):
        display_image(academic_data["Logo"][i], width=100)
        st.write(academic_data["Description"][i])


# Define the data
extension_data = {
    "Brand": ["UDEMY", "ESPM", "ESPM", "Buscapé University", "EBG School", "IAB Brazil"],
    "Logo": ["C:/Users/maula/OneDrive/Desktop/webpage/pages/images/udemy.png",
             "C:/Users/maula/OneDrive/Desktop/webpage/pages/images/espm.jpg",
             "C:/Users/maula/OneDrive/Desktop/webpage/pages/images/espm.jpg",
             "C:/Users/maula/OneDrive/Desktop/webpage/pages/images/buscape.png",
             "C:/Users/maula/OneDrive/Desktop/webpage/pages/images/ebg.png",
             "C:/Users/maula/OneDrive/Desktop/webpage/pages/images/iab.jpg"],
    "Description": ["AI & MACHINE LEARNING FUNDAMENTALS", "AGILE METHODS", "PROGRAMATIC MEDIA PLANNING & PURCHASE", "E-COMMERCE PROFESSIONAL", "GAME METRICS", "DIGITAL MEDIA MANAGEMENT AND PLANNING"]}


with st.expander("Knowledge Extensions"):
    # Display the data in a table
    for i in range(len(extension_data["Description"])):
        display_image(extension_data["Logo"][i], width=100)
        st.write(extension_data["Description"][i])
