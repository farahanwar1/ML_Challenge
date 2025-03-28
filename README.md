# ML_Challenge

## 🚔 Crime Analysis and Prediction Challenge

---

### **Level 1: Exploratory Data Analysis (EDA)**
In this phase, the focus was on understanding and preprocessing the **CityX crime dataset** to extract meaningful insights. Key tasks included:

- **Data Cleaning**: Handling missing values, duplicate records, and data inconsistencies.  
- **Feature Engineering**: Creating new features to improve model performance.  
- **Visualization**: Using **Matplotlib** and **Seaborn** to analyze crime distribution, trends over time, and correlations.  
- **Key Insights**: Identified high-crime areas, peak crime times, and patterns in different crime categories.  

#### 📊 **Data Analysis & Visualization**
- 📌 **Most Common Crimes** – A bar chart visualized the top reported crime categories.  
- 📌 **Crimes by Weekday** – Showed the frequency of crimes across different days.  
- 📌 **Crime Trends Over Time** – A line graph displayed monthly crime fluctuations.  
- 📌 **Crime Heatmap** – Analyzed crime distribution across days and hours using a heatmap.  

---

### **Level 2: Crime Classification Model**
I've successfully built a **crime classification model** using supervised learning to predict crime categories based on descriptions. Various models were tested, and their performance was evaluated using accuracy and F1-score. The steps included:

- **Feature Extraction**: Converting crime descriptions and reports into numerical features using **TF-IDF Vectorization**.  
- **Model Selection**: Experimented with different classifiers (**Logistic Regression, Random Forest, XGBoost, and Naive Bayes**).  
- **Evaluation**: Used **accuracy, precision, recall, and F1-score** to assess model performance.  
- **Outcome**: The final model achieved **[mention accuracy if available]%** accuracy and was saved as a **crime_category_model.pkl** file for later use.  

#### 📊 **Model Performance Results**
- **Logistic Regression**: **Accuracy - 99.68%**, **F1-score - 0.9891**.  
- **Random Forest**: **Accuracy - 99.71%**, **F1-score - 0.9897**.  
- **XGBoost**: **Accuracy - 99.71%**, **F1-score - 0.9897**.  
- **Naive Bayes**: **Accuracy - 99.57%**, **F1-score - 0.9853**.  

---

## **Level 3: Geo-Spatial Mapping & Basic Web UI** 💻
To enhance crime analysis in **CityX**, an interactive **crime mapping dashboard** was developed. The implementation consisted of two parts:

### **Part A: Geo-Spatial Visualization** 🗺️
- An **interactive map** was created using **Tableau Public** to display crime incidents across different locations.
- Various crime visualization techniques were applied, including:
  - **Crime Incident Map** 🗺️: Plots all recorded crime locations.
  - **Bar Chart** 📊: Displays the distribution of crime categories.
  - **Bubble Chart** 🟢: Shows crime counts per district.

### **Part B: Basic Web UI** 🌐
- A **web-based dashboard** was built using Tableau, allowing users to explore crime trends dynamically.
- **Interactive Features**:
  - **Filter by Crime Category**: Select any category desired by clicking on a bar in the bar chart. The map updates to show incidents only for the selected crime type, while the bubble chart reflects crime distribution by district. (Click again on the same bar to remove filtration).
  - **Filter by District**: Select any district desired by clicking on a bubble from the bubble chart. The map displays all crimes in the selected district, while the bar chart updates to show crime distribution by type. (Click again on the same bubble to remove filtration).

---

## **Level 4: Crime Data Analysis & Prediction Web UI** 🌍
### **Overview**
This project provides a web-based interface for crime data analysis and prediction. It includes:
- **PDF Extraction**: Extracting structured crime report data from PDF files.
- **Data Processing & Prediction**: Cleaning the extracted data and predicting crime categories and severity levels.
- **Web UI**: An interactive **Streamlit-based form** to enter crime reports and visualize predictions.

---

### **Installation**
1. **Clone the Repository**
2. **Install Dependencies**
3. **Extract Crime Reports from PDFs**
4. **Train the Machine Learning Model**
5. **Run the Web UI**
6. Launch the Streamlit application with:
   ```bash
   streamlit run app.py
   ```
   This will start the web server and open the form in your browser.

---

### **Instructions**
#### **Level 4 – Part A: Police Report Extraction**
- To extract crime report data from a PDF file, insert the desired file in the following code:
  ```python
  # Define the path to the PDF file
  pdf_path = "police_reports/police_crime_report_1.pdf"
  ```
- The extracted data will be displayed in a structured table format.

#### **Level 4 – Part B: Integration with Classifier**
- This part converts data into a structured format and predicts crime categories and severity using the model from **Level 2**.
- The CSV file will be updated with the extracted crime details.
- To execute, insert the PDF file in the following code:
  ```python
  pdf_file = "police_reports/police_crime_report_1.pdf"  # Update with desired PDF file
  ```

#### **Level 4 – Part C: Enhanced Web UI**
- This part implements a **web interface** displaying a **form** to enter crime details and receive predictions.
- The **predicted category and severity** will be stored in the CSV file **crime_data_with_severity.csv**.
- **How to Run:**
  1. Run the **Python script**. A terminal panel will appear.
  2. Execute the command:
     ```bash
     streamlit run "ML_Level4_Part_C.py"
     ```
  3. The Streamlit app will open in a web browser.
  4. Fill in the **required details** in the form and submit.
  5. The **crime prediction results** will be displayed and updated in the CSV file.

---

### **Web UI Features**
#### **Crime Report Entry Form**
✅ **Inputs:**
- Date & Time (Format: YYYY-MM-DD HH:MM:SS)
- Detailed Description
- Police District
- Incident Location
- Resolution
- Latitude & Longitude

✅ **Outputs:**
- **Predicted Crime Category**
- **Assigned Severity Level**
- **Saved data to** `crime_data_with_severity.csv`

---

### **Additional Notes**
- **Data Storage**: All submitted reports are appended to `crime_data_with_severity.csv`.
- **Error Handling**: The app ensures correct date-time formatting and handles missing input fields.
- **Files Download**: Make sure you downlad all the files in the repository to avoid an errors.

---

### **Dependencies**
Ensure you have the following installed:
- **Python 3.8+**
- **Streamlit**
- **Pandas**
- **Scikit-learn**
- **Joblib**
- **PyMuPDF** (for PDF extraction)

Refer to `requirements.txt` for full package details.🔍


---  

🚀**Thank you for exploring this project!** I hope this tool provides valuable insights for crime analysis and prediction. This project is just the beginning—there's always room for improvement! If you have insights, feedback, or ideas, I'd love to hear them. Let’s innovate together! 🚔✨