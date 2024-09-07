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


def main():
    st.title("How Healthy are your Plants?")
    uploaded_file = st.file_uploader("Upload a JPG or PNG image", type=["jpg", "png"])
    if uploaded_file is not None:
        handle_uploaded_image(uploaded_file)
    camera_image = st.camera_input("Capture an image")
    if camera_image is not None:
        img = Image.open(camera_image)
        calculate_ndvi(img)


if __name__ == "__main__":
    main()