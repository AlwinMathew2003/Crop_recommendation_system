import streamlit as st
import joblib
import wikipedia

# Load the model
models = joblib.load('crop_app')

# Function to fetch crop information from Wikipedia


def get_crop_info(crop_name):
    try:
        page = wikipedia.page(crop_name)
        content = page.content

        # Split content into paragraphs
        paragraphs = content.split('\n')

        # Convert paragraphs to Markdown
        markdown_content = ""
        for paragraph in paragraphs:
            # Check if paragraph starts and ends with "=="
            if paragraph.startswith('==') and paragraph.endswith('=='):
                # Treat it as a heading
                heading = paragraph.strip('= ')
                markdown_content += f"\n## {heading}\n\n"
            else:
                # Treat it as regular text
                markdown_content += f"{paragraph}\n"

        return markdown_content
    except wikipedia.exceptions.PageError:
        return "No information found for this crop."

# Main Streamlit app function

def app():
    st.header("Predict your crop")
    
    # Streamlit sliders for input features
    st.subheader("Enter Feature Values:")
    N = st.slider("Nitrogen (N)", 0.0, 300.0, 150.0, step=0.01)
    P = st.slider("Phosphorus (P)", 0.0, 300.0, 150.0, step=0.01)
    K = st.slider("Potassium (K)", 0.0, 300.0, 150.0, step=0.01)
    temperature = st.slider("Temperature (°C)", -10.0, 50.0, 20.0, step=0.01)
    humidity = st.slider("Humidity (%)", 0.0, 100.0, 50.0, step=0.01)
    ph = st.slider("pH", 0.0, 14.0, 7.0, step=0.01)
    rainfall = st.slider("Rainfall (mm)", 0.0, 500.0, 250.0, step=0.01)
    
    # Predict button
    if st.button("Predict"):
        input_data = [[N, P, K, temperature, humidity, ph, rainfall]]
        prediction = models.predict(input_data)
        crop_name = prediction[0]
        crop_name = crop_name.capitalize()
        st.subheader(f"Predicted Crop: {crop_name}")
        
        # Fetch and display crop information from Wikipedia
        crop_info = get_crop_info(crop_name)
        st.subheader("Crop Information from Wikipedia:")
        st.markdown(crop_info,unsafe_allow_html=True)


