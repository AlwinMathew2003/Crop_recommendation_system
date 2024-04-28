import streamlit as st
from streamlit_option_menu import option_menu
import home, dataAnalysis, models, prediction
import json
from streamlit_lottie import st_lottie 
# Set page title and icon with plant emoji
st.set_page_config(
    page_title="CROP RECOMMENDATION SYSTEM",
    page_icon="🌱"  # Plant emoji as the page icon
)


path = "Animation - 1714327262497.json"

with open(path, "r") as file:
    url = json.load(file)

# Display the Lottie animation in the sidebar

with st.sidebar:
    
    st_lottie(url, 
              reverse=True, 
              height=300, 
              width=300, 
              speed=1, 
              loop=True, 
              quality='high', 
              key='Car')
    st.write("""
    # 🌱 Explore the Best Crops for Your Farm 

    Uncover **optimal crop choices** tailored to your soil nutrients and environmental conditions. Let's find the perfect match for your farm! 🚜🌿
    """, unsafe_allow_html=True)


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        selected = option_menu(
            menu_title=None,
            options=['Home', 'Dataset', 'Model', 'Prediction'],
            icons=['🏠', '📊', '🧪', '💳'],
            default_index=0,
            orientation="horizontal"
        )

        for app in self.apps:
            if selected == app['title']:
                app['function']()

# Instantiate the MultiApp class and run the application
app = MultiApp()

# Add all your apps to the MultiApp instance
app.add_app('Home', home.app)
app.add_app('Dataset', dataAnalysis.app)
app.add_app('Model', models.app)
app.add_app('Prediction', prediction.app)

# Run the application
app.run()
