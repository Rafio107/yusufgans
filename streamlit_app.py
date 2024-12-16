import streamlit as st
from PIL import Image, ImageEnhance

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Page 1: Instructions", "Page 2: Group Members", "Page 3: Image Transformation App"])

# Page 1: Instructions
if page == "Page 1: Instructions":
    st.title("Instructions")
    st.write("""
    Welcome to the Image Transformation App! Follow the instructions below to use the app:
    
    1. Navigate to **Page 3: Image Transformation App** using the sidebar.
    2. Upload an image (supported formats: PNG, JPG, JPEG).
    3. Use the sliders to:
       - Adjust brightness.
       - Rotate the image.
       - Scale the image (resize).
       - Apply skew transformations.
    4. View the resulting image after each transformation.

    Use **Page 2: Group Members** to view the team members of this project.
    """)

    # Upload and Display Logo
    st.write("### Upload and Display Logo")
    logo_file = st.file_uploader("Upload a logo", type=["png", "jpg", "jpeg"], key="logo")
    if logo_file is not None:
        logo = Image.open(logo_file)
        st.image(logo, caption="Project Logo", use_column_width=True)

# Page 2: Group Members
elif page == "Page 2: Group Members":
    st.title("Group Members")
    st.write("""
    This project was developed by the following team members:
    """)

    # Add member images and names
    num_members = st.number_input("Number of group members", min_value=1, max_value=10, value=4, step=1, key="num_members")
    
    for i in range(1, num_members + 1):
        st.write(f"### Member {i}")
        member_name = st.text_input(f"Enter name for Member {i}", key=f"name_{i}")
        member_image = st.file_uploader(f"Upload an image for Member {i}", type=["png", "jpg", "jpeg"], key=f"image_{i}")
        
        if member_name:
            st.write(f"**Name**: {member_name}")
        if member_image:
            member_photo = Image.open(member_image)
            st.image(member_photo, caption=f"{member_name}'s Photo", use_column_width=True)

    st.write("Thank you for using our app!")

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
