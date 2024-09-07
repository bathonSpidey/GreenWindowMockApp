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




# Streamlit app
def main():
    st.title("RAISE: Demo NDVI Calculator")

    # Centering the buttons
    open_camera = st.button("Open Camera")
    uploaded_file = st.file_uploader("Upload a JPG or PNG image", type=["jpg", "png"])

    if 'camera_opened' not in st.session_state:
        st.session_state['camera_opened'] = False

    # Placeholder for video feed
    frame_window = st.empty()
    if uploaded_file is not None:
        handle_uploaded_image(uploaded_file)

    if open_camera:
        st.session_state['camera_opened'] = True

    # When camera is opened
    if st.session_state['camera_opened']:
        cap = cv2.VideoCapture(0)

        # Add Capture Image button
        capture_image = st.button("Capture Image")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                st.write("Unable to open camera.")
                break

            # Convert to RGB and display the frame
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_window.image(frame_rgb)

            if capture_image:
                # Show NDVI message and close the camera
                calculate_ndvi()
                frame_window.empty()
                st.session_state['camera_opened'] = False
                break
        if st.session_state['camera_opened'] == False:
            st.write("Realeasing camera.")
            cap.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    main()