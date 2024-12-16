import streamlit as st
from PIL import Image, ImageEnhance

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Page 1: Linear Algebra Group 4", "Page 2: Group Members", "Page 3: Image Transformation App"])

# Page 1: Linear Algebra Group 4
if page == "Page 1: Linear Algebra Group 4":
    # Logo Section
    st.write("### Upload and Display Logo")
    logo_file = st.file_uploader("Upload a logo", type=["png", "jpg", "jpeg"], key="logo")
    if logo_file is not None:
        logo = Image.open(logo_file)
        st.image(logo, caption="Project Logo", use_column_width=True)

    # Title and Description
    st.title("Linear Algebra Group 4")
    st.write("""
    Welcome to the Linear Algebra Group 4 App! This app contains the following features:
    
    1. View the project members on **Page 2: Group Members**.
    2. Perform image transformations on **Page 3: Image Transformation App**.
    """)

# Page 2: Group Members
elif page == "Page 2: Group Members":
    st.title("Group Members")
    st.write("### Meet the Team Members")

    # Display Hardcoded Member Names
    members = [
        {"name": "Member 1: Alice", "photo": None},
        {"name": "Member 2: Bob", "photo": None},
        {"name": "Member 3: Charlie", "photo": None},
        {"name": "Member 4: Diana", "photo": None}
    ]

    # Iterate through members to display their names and upload sections
    for member in members:
        st.write(f"**{member['name']}**")
        uploaded_photo = st.file_uploader(f"Upload photo for {member['name']}", type=["png", "jpg", "jpeg"], key=f"photo_{member['name']}")
        if uploaded_photo:
            photo = Image.open(uploaded_photo)
            st.image(photo, caption=f"{member['name']}'s Photo", use_column_width=True)

# Page 3: Image Transformation App
elif page == "Page 3: Image Transformation App":
    st.title("Image Transformation App")
    st.write("Upload an image and adjust transformations using the sliders.")

    # Upload Image
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], key="image_transformation")
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
