Heart Attack Risk Dashboard
This Streamlit web application provides insights into heart attack risk based on a dataset containing demographic and health-related attributes from individuals across India. Users can interactively filter and analyze data based on age, gender, and state.

Features
Displays the complete dataset for reference.

Calculates and shows the average heart attack risk based on gender.

Interactive search: filter individuals based on age and gender.

View the corresponding states for the filtered results.

Dataset
The app uses a CSV file named heart_attack_prediction_india.csv, which should be placed in the root directory. The dataset is expected to have the following key columns:

Age

Gender

Heart_Attack_Risk

State_Name

Note: Ensure that the column names in the CSV match exactly as used in the code.

How to Run Locally
Clone this repository:

bash
Copy
Edit
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install dependencies (preferably in a virtual environment):

bash
Copy
Edit
pip install streamlit pandas
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Usage
The dashboard displays full data and gender-based risk averages.

Use the input fields to specify an age and gender.

The app filters the data and shows relevant results including the state(s) of the matched records.

Folder Structure
Copy
Edit
├── app.py
├── heart_attack_prediction_india.csv
└── README.md
License
This project is for educational and research purposes only.
