import streamlit as st
from PIL import Image

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Page 1: Group Logo", "Page 2: Group Members", "Page 3: Image Transformation App"])

# Page 1: Group Logo
if page == "Page 1: Group Logo":
    # Display logo warning first
    try:
        logo = Image.open("logo.jpg")  # Replace with your logo file name
        st.image(logo, caption="Group Logo", width=300)
    except FileNotFoundError:
        st.warning("Logo not found! Please make sure 'logo.jpg' is in the directory.")
    
    # Title and content
    st.title("Linear Group 4")
    st.write("""
    Welcome to the Linear Algebra Group 4 App! Below is the group logo:
    """)

# Page 2: Group Members
elif page == "Page 2: Group Members":
    st.title("Group Members")
    st.write("### Meet the Team Members")

    # List of group members with images
    members = [
        {"name": "MUHAMMAD YUSUF IRSYADULLOH (004202300040)", "role": "Leader", "photo": "Muka yusuf.jpg"},
        {"name": "SYARIFA NURAINI (004202300028)", "role": "Member", "photo": "Muka syarifa.jpg"},
        {"name": "MARIA DIANATA\t(004202300084)", "role": "Member", "photo": "Muka Maria.jpg"},
        {"name": "BUNGA GEMBIRA\t(004202300037)", "role": "Member", "photo": "Muka Bunga.jpg"}
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
    st.write("Upload an image and perform transformations using sliders.")

    # File uploader for image input
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_column_width=True)

        # Image transformation options
        st.write("### Transformation Options")
        rotation_angle = st.slider("Rotate Image (degrees)", -180, 180, 0)
        resize_width = st.slider("Resize Width", 50, 500, image.width)
        resize_height = st.slider("Resize Height", 50, 500, image.height)

        # Apply transformations
        transformed_image = image.rotate(rotation_angle).resize((resize_width, resize_height))

        # Display transformed image
        st.image(transformed_image, caption="Transformed Image", use_column_width=True)
