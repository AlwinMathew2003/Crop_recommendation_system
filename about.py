# st.image("Image-Crop-Recommendation@1x-1.png", width=700)

# st.markdown(
#     """
#     <style>
#     .sidebar-heading {
#         text-align: center;
#         margin-top: 0px;
#         border-radius:23px;
#         transition: background-color 0.3s, color 0.3s;
#     }

#     .sidebar-heading:hover {
#         border-radius:23px;
#         background-color: #DE3163; /* Change background color on hover */
#         color: white; /* Change text color on hover */
#         cursor: pointer;
        
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )



# st.sidebar.markdown('<h1 class="sidebar-heading" >HOME</h1>', unsafe_allow_html=True)
# st.sidebar.markdown('<h1 class="sidebar-heading" >ABOUT</h1>', unsafe_allow_html=True)
# st.sidebar.markdown('<h1 class="sidebar-heading">CONTACT</h1>', unsafe_allow_html=True)
# st.sidebar.markdown('<h1 class="sidebar-heading">DATA ANALYSIS</h1>', unsafe_allow_html=True)
# st.sidebar.markdown('<h1 class="sidebar-heading">PREDICTION</h1>', unsafe_allow_html=True)

# st.write("""
#     ## Welcome to the Crop Recommendation System!

#     This system helps farmers make **informed decisions** about which crops to grow based on various factors such as soil type, climate, and crop characteristics.

#     ### Enhanced Decision-Making:

#     The **Crop Recommendation System** leverages cutting-edge technology to provide farmers with **data-driven insights** into optimal crop selection. By analyzing a variety of factors such as soil type, climate conditions, and crop characteristics, the system assists farmers in making **informed decisions** about which crops to cultivate on their farms. This process helps optimize crop selection, ensuring that farmers choose crops that are **well-suited to their specific agricultural environment**.

#     ### Maximizing Yield and Profitability:

#     One of the primary benefits of the **Crop Recommendation System** is its ability to **maximize crop yield** and **profitability** for farmers. By recommending crops that are best-suited to the farm's conditions, including soil quality, temperature, and rainfall patterns, the system helps farmers achieve higher yields and improve their overall profitability. Additionally, by selecting crops with **higher yield potential** and **market demand**, farmers can enhance their revenue and **financial sustainability**.

#     ### Resource Efficiency:

#     Another significant advantage of the **Crop Recommendation System** is its ability to promote **resource efficiency** in agriculture. By recommending crops that require optimal levels of water, nutrients, and other resources, the system helps farmers minimize resource wastage and improve resource utilization efficiency. This not only **reduces input costs** for farmers but also contributes to **environmental sustainability** by conserving water and other natural resources.

#     ### Risk Mitigation:

#     The **Crop Recommendation System** plays a crucial role in **mitigating risks** associated with agricultural production. By **diversifying crop selection** based on comprehensive recommendations, farmers can reduce their vulnerability to environmental factors such as droughts, pests, and diseases. Additionally, by selecting crops with different **planting seasons** and **maturity periods**, farmers can spread their risk across multiple crops, thereby minimizing the impact of adverse weather conditions or market fluctuations on their overall crop yield and income.

#     ### Empowering Farmers:

#     Overall, the **Crop Recommendation System** serves as a valuable tool for **empowering farmers** to make informed decisions about crop selection and agricultural management. By providing **personalized recommendations** based on scientific analysis and real-time data, the system enables farmers to optimize their farming practices, **maximize productivity**, and **improve their livelihoods**. Ultimately, by harnessing the power of **technology** and **data analytics**, the **Crop Recommendation System** contributes to the **advancement** and **sustainability** of agriculture, benefiting farmers and agricultural communities worldwide.
# """)

class multiApp:
    def _init_(self):
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

# Instantiate the multiApp class and run the application