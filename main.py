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
    st.title("Info")
    st.write("""
    Willkommen bei der App Plant Health Checker!

    Mit dieser App können Sie die Gesundheit Ihrer Pflanzen anhand eines Bildes beurteilen. 
    Durch die Analyse der Pixel im Bild ermöglicht die App eine schnelle und einfache Bewertung der Pflanzengesundheit.
    
    Für weitere Informationen wenden Sie sich an info@raiseagri.com

    **Wie es funktioniert:**
    - Laden Sie ein Bild Ihrer Pflanze hoch oder nehmen Sie es auf.
    - Die App analysiert die Menge an Grün im Bild und berechnet einen Prozentsatz, der die Pflanzengesundheit darstellt.

    Die NDVI-Technik (Normalized Difference Vegetation Index) wird verwendet, um die Pflanzengesundheit anhand der Grünintensität 
    im Bild.
    """)
    st.error("**Haftungsausschluss:** Dieses Tool ist eine grundlegende Annäherung und kein Ersatz für eine fachliche Beratung."
             "Dies ist eine Demo-App, um die Möglichkeiten unseres Tools zu zeigen. "
             "Für die Vollversion wenden Sie sich bitte an info@raiseagri.com."
             " Wenn Sie sich Sorgen um Ihre Pflanzen machen, ist es immer am besten, einen Gartenbauexperten zu Rate zu ziehen oder uns zu kontaktieren."
             )


def main_page():
    st.title("How Healthy Are Your Plants?")
    about_page()

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
    main_page()


if __name__ == "__main__":
    main()