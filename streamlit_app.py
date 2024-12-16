import streamlit as st
from PIL import Image

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Page 1: Linear Algebra Group 4", "Page 2: Group Members", "Page 3: Image Transformation App"])

# Page 1: Linear Algebra Group 4
if page == "Page 1: Linear Algebra Group 4":
    st.title("Linear Algebra Group 4")
    st.write("""
    Welcome to the Linear Algebra Group 4 App! This app contains the following features:
    
    1. View the project members on **Page 2: Group Members**.
    2. View group member images on **Page 3: Image Transformation App**.
    """)

    # Display logo
    try:
        logo = Image.open("logo.jpg")  # Replace with your logo file name
        st.image(logo, caption="Group Logo", width=300)
    except FileNotFoundError:
        st.warning("Logo not found! Please make sure 'logo.jpg' is in the directory.")

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
    st.write("View group member images below:")

    # List of group members with images
    members = [
        {"name": "MUHAMMAD YUSUF IRSYADULLOH (004202300040)", "photo": "Muka yusuf.jpg"},
        {"name": "SYARIFA NURAINI (004202300028)", "photo": "Muka syarifa.jpg"},
        {"name": "MARIA DIANATA\t(004202300084)", "photo": "Muka Maria.jpg"},
        {"name": "BUNGA GEMBIRA\t(004202300037)", "photo": "Muka Bunga.jpg"}
    ]

    # Display each member's photo
    for member in members:
        st.write(f"**{member['name']}**")
        try:
            photo = Image.open(member['photo'])
            st.image(photo, caption=f"{member['name']}", width=300)
        except FileNotFoundError:
            st.warning(f"Photo for {member['name']} not found!")
