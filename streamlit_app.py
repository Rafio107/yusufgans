import streamlit as st
from PIL import Image

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Page 1: Linear Algebra Group 4", "Page 2: Group Members", "Page 3: Image Transformation App"])

# Page 1: Linear Algebra Group 4
if page == "Page 1: Linear Algebra Group 4":
    # Upload and Display Logo
    st.write("### Upload and Display Logo")
    logo_file = st.file_uploader("Upload a logo", type=["png", "jpg", "jpeg"], key="logo")
    if logo_file is not None:
        logo = Image.open(logo_file)
        st.image(logo, caption="Project Logo", width=200)

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

    # List of group members with images
    members = [
        {"name": "MUHAMMAD YUSUF IRSYADULLOH (004202300040)", "role": "Leader", "photo": "Muka yusuf.jpg"},
        {"name": "SYARIFA NURAINI (004202300028)", "role": "Member", "photo": "Muka syarifa.jpg"},
        {"name": "MARIA DIANATA (004202300084)", "role": "Member", "photo": "Muka Maria.jpg"},
        {"name": "BUNGA GEMBIRA (004202300037)", "role": "Member", "photo": "Muka Bunga.jpg"}
    ]

    # Display each member's photo and role
    for member in members:
        st.write(f"**{member['name']}** - {member['role']}")
        try:
            photo = Image.open(member['photo'])
            st.image(photo, caption=f"{member['name']}", width=150)
        except FileNotFoundError:
            st.warning(f"Photo for {member['name']} not found!")

# Page 3: Image Transformation App
elif page == "Page 3: Image Transformation App":
    st.title("Image Transformation App")
    st.write("Upload an image and adjust transformations using the sliders.")

    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], key="image_transformation")
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_column_width=True)
