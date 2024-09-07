import streamlit as st
import cv2
from PIL import Image
import random

def calculate_ndvi():
    ndvi_value = random.random()
    if ndvi_value <= 0.4:
        st.error(f"The NDVI is {ndvi_value:.2f}. Either the plant is growing or it requires love and care.")
    else:
        st.success(f"The NDVI is {ndvi_value:.2f}. The plant is healthy. Keep it up!")

def handle_uploaded_image(uploaded_file):
    image = Image.open(uploaded_file)
    calculate_ndvi()


def main():
    st.title("RAISE: Demo NDVI Calculator")
    open_camera = st.button("Open Camera")
    uploaded_file = st.file_uploader("Upload a JPG or PNG image", type=["jpg", "png"])

    if uploaded_file is not None:
        handle_uploaded_image(uploaded_file)

    if open_camera:
        st.session_state['camera_opened'] = True

    camera_image = st.camera_input("Capture an image")
    if camera_image is not None:
        img = Image.open(camera_image)
        calculate_ndvi()


if __name__ == "__main__":
    main()