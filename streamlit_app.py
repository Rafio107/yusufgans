import streamlit as st
from PIL import Image, ImageEnhance
from pathlib import Path

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

    # Data anggota kelompok
    members = [
        {"name": "Alice", "photo": "Alice.jpg", "position": "Leader"},
        {"name": "Bob", "photo": "Bob.jpg", "position": "Data Analyst"},
        {"name": "Charlie", "photo": "Charlie.jpg", "position": "Developer"},
        {"name": "Diana", "photo": "Diana.jpg", "position": "Designer"}
    ]

    # Display members in grid layout
    cols = st.columns(4)  # Membuat 4 kolom untuk anggota kelompok

    for idx, member in enumerate(members):
        with cols[idx % 4]:  # Distribusi anggota ke dalam kolom
            # Periksa apakah file gambar ada
            photo_path = Path(member["photo"])
            if photo_path.exists():
                # Tampilkan gambar jika tersedia
                image = Image.open(photo_path)
                st.image(image, caption=member["name"], use_column_width=True)
                st.markdown(f"**{member['position']}**", unsafe_allow_html=True)
            else:
                # Peringatan jika gambar tidak ditemukan
                st.warning(f"Photo not found for {member['name']}!")

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
