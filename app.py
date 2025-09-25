import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- Load Models, Encoders, and Mappings ---
try:
    crop_model = joblib.load('crop_prediction_model.pkl')
    fertilizer_model = joblib.load('fertilizer_prediction_model.pkl')
    le_district = joblib.load('district_name_encoder.pkl')
    le_soil = joblib.load('soil_color_encoder.pkl')
    le_crop = joblib.load('crop_encoder.pkl')
    le_fertilizer = joblib.load('fertilizer_encoder.pkl')
    link_mapping = joblib.load('crop_to_link_mapping.pkl')
except FileNotFoundError:
    st.error("Model or encoder files not found. Please run the notebook to generate them.")
    st.stop()

# --- Initialize Session State ---
# This is to store the predicted crop between button clicks
if 'predicted_crop' not in st.session_state:
    st.session_state.predicted_crop = None

# --- Page Configuration ---
st.set_page_config(page_title="Crop & Fertilizer Recommender", layout="wide")

# --- Custom CSS for Styling ---
st.markdown("""
<style>
    .main {
        background-color: #F5F5F5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 24px;
        border: none;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)

# --- App Title and Description ---
st.title('🌾 Advanced Crop & Fertilizer Recommendation System')
st.markdown("Enter your field's details to receive a tailored crop and fertilizer recommendation.")

# --- Input Fields Arranged in Columns ---
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Soil & Environment")
    nitrogen = st.number_input('Nitrogen (N) Content', min_value=0, max_value=150, value=75)
    phosphorus = st.number_input('Phosphorus (P) Content', min_value=0, max_value=100, value=50)
    potassium = st.number_input('Potassium (K) Content', min_value=0, max_value=150, value=100)
    
with col2:
    st.header("Climate")
    ph = st.slider('Soil pH Level', 3.0, 9.0, 6.5, 0.1)
    rainfall = st.number_input('Rainfall (in mm)', min_value=0, value=1000)
    temperature = st.slider('Temperature (°C)', 0, 50, 25)

with col3:
    st.header("Location")
    district_name = st.selectbox('District Name', le_district.classes_)
    soil_color = st.selectbox('Soil Color', le_soil.classes_)

# --- STEP 1: CROP PREDICTION ---
if st.button('Get Crop Recommendation'):
    try:
        input_data_crop = pd.DataFrame({
            'District_Name': [le_district.transform([district_name])[0]],
            'Soil_color': [le_soil.transform([soil_color])[0]],
            'Nitrogen': [nitrogen],
            'Phosphorus': [phosphorus],
            'Potassium': [potassium],
            'pH': [ph],
            'Rainfall': [rainfall],
            'Temperature': [temperature]
        })
        
        predicted_crop_encoded = crop_model.predict(input_data_crop)
        # Store the predicted crop name in session state
        st.session_state.predicted_crop = le_crop.inverse_transform(predicted_crop_encoded)[0]

    except Exception as e:
        st.error(f"An error occurred during crop prediction: {e}")

# --- Display Crop Recommendation and Allow Manual Override ---
if st.session_state.predicted_crop:
    st.markdown("---")
    st.success(f'### Step 1: Recommended Crop 👉 **{st.session_state.predicted_crop}**')
    
    video_link = link_mapping.get(st.session_state.predicted_crop)
    if video_link:
        st.markdown(f"**Planting Guide:** [{video_link}]({video_link})")

    st.markdown("---")
    st.write("### Step 2: Confirm or Change Your Crop")
    
    # Find the index of the predicted crop to set it as the default in the selectbox
    crop_options = list(le_crop.classes_)
    predicted_crop_index = crop_options.index(st.session_state.predicted_crop)
    
    # Create the selectbox for manual override
    final_crop = st.selectbox(
        'Select the final crop for fertilizer recommendation:',
        options=crop_options,
        index=predicted_crop_index
    )

    # --- STEP 2: FERTILIZER PREDICTION ---
    if st.button('Get Fertilizer Recommendation'):
        try:
            # Encode the final selected crop (either predicted or manually chosen)
            final_crop_encoded = le_crop.transform([final_crop])[0]
            
            input_data_fertilizer = pd.DataFrame({
                'District_Name': [le_district.transform([district_name])[0]],
                'Soil_color': [le_soil.transform([soil_color])[0]],
                'Nitrogen': [nitrogen],
                'Phosphorus': [phosphorus],
                'Potassium': [potassium],
                'pH': [ph],
                'Rainfall': [rainfall],
                'Temperature': [temperature],
                'Crop': [final_crop_encoded]
            })

            predicted_fertilizer_encoded = fertilizer_model.predict(input_data_fertilizer)
            predicted_fertilizer_name = le_fertilizer.inverse_transform(predicted_fertilizer_encoded)[0]

            st.success(f'### Final Recommendation: For **{final_crop}**, the best fertilizer is 👉 **{predicted_fertilizer_name}**')

        except Exception as e:
            st.error(f"An error occurred during fertilizer prediction: {e}")