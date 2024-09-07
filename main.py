import streamlit as st
import cv2
from PIL import Image
import random
import numpy as np


def calculate_ndvi(image):
    image_cv = np.array(image)
    hsv_image = cv2.cvtColor(image_cv, cv2.COLOR_RGB2HSV)
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
    green_pixels = np.count_nonzero(green_mask)
    total_pixels = green_mask.size
    green_percentage = (green_pixels / total_pixels) * 100
    if green_percentage <= 40:
        st.error(
            f"The health {green_percentage:.2f}%. Either the plant is growing or it requires love and care.")
    else:
        st.success(f"The health is {green_percentage:.2f}%. The plant is healthy. Keep it up!")

def handle_uploaded_image(uploaded_file):
    image = Image.open(uploaded_file)
    calculate_ndvi(image)

def about_page():
    st.title("About This App")
    st.write("""
    Welcome to the Plant Health Checker App!

    This app allows you to assess the health of your plants using an image. 
    By analyzing the pixels in the image, the app provides a quick and simple assessment of plant health.
    
    For more details contact info@raiseagri.com

    **How it works:**
    - Upload or capture an image of your plant.
    - The app analyzes the amount of green in the image and calculates a percentage that represents plant health.

    The NDVI (Normalized Difference Vegetation Index) technique is used to assess plant health based on green intensity 
    in the image.
    """)
    st.error("**Disclaimer:** This tool is a basic approximation and is not a replacement for expert advice. "
             "This is a demo app to show case the capabilities of our tool. For the full version please contact info@raiseagri.com. "
             "If you're concerned about your plants,it's always best to consult with a horticultural expert or contact us. ")


def main_page():
    st.title("How Healthy Are Your Plants?")

    # Upload image
    uploaded_file = st.file_uploader("Upload a JPG or PNG image", type=["jpg", "png"])
    if uploaded_file is not None:
        handle_uploaded_image(uploaded_file)

    # Capture image from camera
    camera_image = st.camera_input("Capture an image")
    if camera_image is not None:
        img = Image.open(camera_image)
        calculate_ndvi(img)
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Plant Health Checker", "About"])

    if page == "Plant Health Checker":
        main_page()
    elif page == "About":
        about_page()


if __name__ == "__main__":
    main()