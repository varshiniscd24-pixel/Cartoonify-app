import streamlit as st
import cv2
import numpy as np
from PIL import Image

def cartoonify_image(image):
    # Convert to grayscale + blur
    g = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    g = cv2.medianBlur(g, 5)

    # Edges
    e = cv2.adaptiveThreshold(g, 255,
                              cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY, 9, 9)

    # Smooth color
    c = cv2.bilateralFilter(image, 9, 250, 250)

    # Combine
    cartoon = cv2.bitwise_and(c, c, mask=e)
    return cartoon

st.title("🎨 Cartoonify Your Image")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read image
    img = Image.open(uploaded_file)
    img = np.array(img)

    # Cartoonify
    cartoon = cartoonify_image(img)

    # Show results
    st.image([img, cartoon], caption=["Original", "Cartoonified"], width=300)
