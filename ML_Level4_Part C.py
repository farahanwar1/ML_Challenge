import streamlit as st
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from datetime import datetime

# Load trained model and vectorizer
model = joblib.load("crime_category_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def assign_severity(category):
    severity_mapping = {
        "NON-CRIMINAL": 1, "SUSPICIOUS OCC": 1, "MISSING PERSON": 1, "RUNAWAY": 1, "RECOVERED VEHICLE": 1,
        "WARRANTS": 2, "OTHER OFFENSES": 2, "VANDALISM": 2, "TRESPASS": 2, "DISORDERLY CONDUCT": 2, "BAD CHECKS": 2,
        "LARCENY/THEFT": 3, "VEHICLE THEFT": 3, "FORGERY/COUNTERFEITING": 3, "DRUG/NARCOTIC": 3,
        "STOLEN PROPERTY": 3, "FRAUD": 3, "BRIBERY": 3, "EMBEZZLEMENT": 3,
        "ROBBERY": 4, "WEAPON LAWS": 4, "BURGLARY": 4, "EXTORTION": 4,
        "KIDNAPPING": 5, "ARSON": 5
    }
    return severity_mapping.get(category, -1)

# Web App Title
st.title("Crime Report Entry & Prediction")

# User Input Form
with st.form("crime_form"):
    date_time = st.text_input("Date & Time (YYYY-MM-DD HH:MM:SS)")
    description = st.text_area("Detailed Description")
    police_district = st.text_input("Police District")
    incident_location = st.text_input("Incident Location")
    resolution = st.text_input("Resolution")
    latitude = st.text_input("Latitude")
    longitude = st.text_input("Longitude")
    submit_button = st.form_submit_button("Submit Report")

if submit_button:
    # Validate date format
    try:
        day_of_week = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").strftime("%A")
    except ValueError:
        st.error("Invalid Date & Time format. Use YYYY-MM-DD HH:MM:SS")
        st.stop()

    # Predict Crime Category
    predicted_category = model.predict([description])[0]
    predicted_severity = assign_severity(predicted_category)

    # Save to CSV
    csv_file = "crime_data_with_severity.csv"
    new_row = {
        "Dates": date_time,
        "Category": predicted_category,
        "Descript": description,
        "DayOfWeek": day_of_week,
        "PdDistrict": police_district,
        "Resolution": resolution,
        "Address": incident_location,
        "Latitude (Y)": latitude,
        "Longitude (X)": longitude,
        "Severity": predicted_severity
    }
    
    existing_df = pd.read_csv(csv_file)
    updated_df = pd.concat([existing_df, pd.DataFrame([new_row])], ignore_index=True)
    updated_df.to_csv(csv_file, index=False)
    
    # Display Results
st.success("Crime report submitted successfully!")
st.write("### Prediction Results")
st.write(f"**Predicted Category:** {predicted_category}")
st.write(f"**Severity Level:** {predicted_severity}")

# Display small success message about CSV update
st.markdown('<p style="font-size:12px; color:gray;">✅ Data successfully stored in the report CSV file.</p>', unsafe_allow_html=True)



