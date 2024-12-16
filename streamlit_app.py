import streamlit as st
from PIL import Image, ImageEnhance
import numpy as np

# Title and Description
st.title("Image Transformation App")
st.write("Upload an image and adjust transformations using the sliders.")

# Upload Image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    # Open image using Pillow
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    # Brightness Slider
    brightness = st.slider("Adjust Brightness", 0.1, 3.0, 1.0)
    enhancer = ImageEnhance.Brightness(image)
    bright_image = enhancer.enhance(brightness)
    st.image(bright_image, caption="Brightness Adjusted", use_column_width=True)

    # Rotation Slider
    angle = st.slider("Rotate Image (Degrees)", -180, 180, 0)
    rotated_image = bright_image.rotate(angle, expand=True)
    st.image(rotated_image, caption="Rotated Image", use_column_width=True)

    # Scaling Slider
    scale = st.slider("Scale Image", 0.1, 3.0, 1.0)
    new_size = (int(rotated_image.width * scale), int(rotated_image.height * scale))
    scaled_image = rotated_image.resize(new_size, Image.Resampling.LANCZOS)
    st.image(scaled_image, caption="Scaled Image", use_column_width=True)

    # Skewing Example (using Affine Transform in Pillow)
    skew_factor = st.slider("Skew Factor", -0.5, 0.5, 0.0)
    width, height = scaled_image.size
    skew_matrix = (1, skew_factor, 0, skew_factor, 1, 0)
    skewed_image = scaled_image.transform((width, height), Image.AFFINE, skew_matrix)
    st.image(skewed_image, caption="Skewed Image", use_column_width=True)
