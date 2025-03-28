## LEVEL 4 PART C


import streamlit as st      # Importing Streamlit for the web interface
import pandas as pd     # Importing Pandas for data manipulation
import joblib       # Importing joblib to load pre-trained models and vectorizers
from sklearn.feature_extraction.text import TfidfVectorizer     # Importing TF-IDF vectorizer to process text data
from datetime import datetime       # Importing datatime to handle date-time formats

# Load trained model and vectorizer
model = joblib.load("crime_category_model.pkl")     # Load the pre-trained crime category model
vectorizer = joblib.load("vectorizer.pkl")          # Load the pre-trained TF-IDF vectorizer

# Function to assign severity level based on the crime category
def assign_severity(category):
    severity_mapping = {
        "NON-CRIMINAL": 1, "SUSPICIOUS OCC": 1, "MISSING PERSON": 1, "RUNAWAY": 1, "RECOVERED VEHICLE": 1,
        "WARRANTS": 2, "OTHER OFFENSES": 2, "VANDALISM": 2, "TRESPASS": 2, "DISORDERLY CONDUCT": 2, "BAD CHECKS": 2,
        "LARCENY/THEFT": 3, "VEHICLE THEFT": 3, "FORGERY/COUNTERFEITING": 3, "DRUG/NARCOTIC": 3,
        "STOLEN PROPERTY": 3, "FRAUD": 3, "BRIBERY": 3, "EMBEZZLEMENT": 3,
        "ROBBERY": 4, "WEAPON LAWS": 4, "BURGLARY": 4, "EXTORTION": 4,
        "KIDNAPPING": 5, "ARSON": 5
    }
    # Return the severity level for the given category, default to -1 for unknown categories
    return severity_mapping.get(category, -1)

# Web App Title - Setting the title of the app
st.title("Crime Report Entry & Prediction")

# User Input Form - Creating aa form for the user to input crime report data 
with st.form("crime_form"):
    # From fields for user input
    date_time = st.text_input("Date & Time (YYYY-MM-DD HH:MM:SS)")  # Date and time input
    description = st.text_area("Detailed Description")          # Crime descroption input
    police_district = st.text_input("Police District")          # Police district input
    incident_location = st.text_input("Incident Location")      # Incident location input
    resolution = st.text_input("Resolution")                # Resolution of the case input
    latitude = st.text_input("Latitude")                # Latitude input
    longitude = st.text_input("Longitude")              # Longitude input 
    submit_button = st.form_submit_button("Submit Report")          # Submit button for form submission

# If the form is submitted 
if submit_button:
    # Validate the date format entered by the user
    try:
        # Convert the date-time string to a day of the week (e.g., Moday, Tuesday)
        day_of_week = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").strftime("%A")          
    except ValueError:
        # If date format is invalid, show an error message and stop further execution 
        st.error("Invalid Date & Time format. Use YYYY-MM-DD HH:MM:SS")
        st.stop()

    # Predict Crime Category based on the description using the pre-trained model
    predicted_category = model.predict([description])[0]
    
    # Assign severity based on the predicted category
    predicted_severity = assign_severity(predicted_category)

    # Define the CSV file path to store the crime report data
    csv_file = "crime_data_with_severity.csv"
    
    # Create a new row with the extracted and predicted data
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
    
    
    # REad the existing crime report CSV file
    existing_df = pd.read_csv(csv_file)
    
    # Add the new row of data to the existing dataframe
    updated_df = pd.concat([existing_df, pd.DataFrame([new_row])], ignore_index=True)
    
    # Save the updated dataframe back to the CSV file
    updated_df.to_csv(csv_file, index=False)
    
    
    # Display a success message 
st.success("Crime report submitted successfully!")

    # Display the predicted results
st.write("### Prediction Results")
st.write(f"**Predicted Category:** {predicted_category}")
st.write(f"**Severity Level:** {predicted_severity}")

# Display small success message about CSV update
st.markdown('<p style="font-size:12px; color:gray;">✅ Data successfully stored in the report CSV file.</p>', unsafe_allow_html=True)




