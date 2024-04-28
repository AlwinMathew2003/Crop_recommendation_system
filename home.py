import streamlit as st
from streamlit_lottie import st_lottie 
import json
def app():
    # Title
    st.title("Crop Recommendation System")

    st.image("Image-Crop-Recommendation@1x-1.png", width=700)
    
  
    # path = "Animation - 1714316208073.json"
    # with open(path,"r") as file: 
    #     url = json.load(file) 
    
    # st_lottie(url, 
    # reverse=True, 
    # height=300, 
    # width=300, 
    # speed=1, 
    # loop=True, 
    # quality='high', 
    # key='Car'
    # )
  
    # Introduction
    st.write("""
    ## Welcome to the Crop Recommendation System!

    This system is designed to assist farmers in making informed decisions about which crops to plant based on various factors 
    such as soil nutrients, temperature, humidity, pH, and rainfall.

    Farmers can use this system to optimize their crop selection process and improve agricultural productivity.


    ---""")

    # Benefits for Farmers
    st.write("""
    ## Benefits for Farmers
    ![Fields](https://d1g9yur4m4naub.cloudfront.net/image-handler/picture/2021/11/shutterstock_1090514927.jpg)

    - **Increase Yield:** By selecting the most suitable crops based on environmental conditions, farmers can increase their yield and maximize profits.

    - **Reduce Risk:** With data-driven recommendations, farmers can mitigate risks associated with crop failure due to unfavorable environmental conditions.

    - **Resource Optimization:** Efficient use of resources such as water, fertilizer, and land leads to sustainable agricultural practices and cost savings.

    - **Improved Decision Making:** Access to insights from data analysis helps farmers make informed decisions, leading to better crop management and planning.

    ---""")

    # Features
    st.write("""
    ## Features
    """)

    path = "Animation - 1714315657162.json"
    with open(path, "r") as file:
        url = json.load(file)

    # Display Lottie animation and text side by side using Streamlit columns
    col1, col2 = st.columns([2, 2])  # Adjust column widths as needed

    with col1:
        st_lottie(url,
                reverse=True,
                height=300,
                width=300,
                speed=1,
                loop=True,
                quality='high',
                key='Car1')

    with col2:
        st.write("""
        ### 1. Data Analysis
        Explore the dataset containing information about soil nutrients and environmental factors.

        ### 2. Crop Recommendation
        Input the values for soil nutrients and environmental factors to get recommendations on suitable crops to plant.

        ### 3. Data Visualization
        Visualize the dataset and analysis results using interactive charts and graphs.

        ---""")


    # How to Use
    st.write("""
    ## How to Use

    1. Navigate to the respective sections using the sidebar.
    2. In the Data Analysis section, you can view the dataset's summary statistics and correlation matrix.
    3. Use the Crop Recommendation section to input the values for soil nutrients and environmental factors.
    4. Get recommendations on suitable crops based on the input values.
    5. Explore the Data Visualization section to visualize the dataset and analysis results using interactive charts and graphs.


    Feel free to explore and utilize the features of the Crop Recommendation System to enhance your farming practices!

    ---""")

    # About
    st.write("""
    ## About

    This Crop Recommendation System is developed to empower farmers with data-driven insights for crop selection 
    and improve agricultural decision-making.

    For any queries or feedback, please contact us at [smartfarming@gmail.com](mailto:email@example.com).



    ---""")


