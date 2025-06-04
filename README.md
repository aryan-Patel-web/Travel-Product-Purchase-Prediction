# 🚀 Travel Product Purchase Prediction

A Flask-based web app that predicts whether a customer will purchase a travel product based on their profile, pitch experience, and other relevant features. The app uses a machine learning model (`RandomForestClassifier`) trained on structured customer interaction data.

---

## 📌 Project Overview

This project predicts customer intent to buy a travel product using a form input. The machine learning model is pre-trained and saved using `joblib`.

- Backend: Flask
- Frontend: HTML/CSS (Form UI)
- ML Model: Random Forest (or other, from `model.ipynb`)
- Preprocessing: Using Scikit-Learn pipelines

---

## 🛠️ Installation & Setup

### 1. Clone the Repository


git clone https://github.com/yourusername/travel-purchase-predictor.git
cd travel-purchase-predictor


 Install Required Packages

 flask
pandas
scikit-learn
joblib


🧪 Sample Input (Will NOT Buy Product)
You can test the app using the following input values:

Field	Value
Customer ID	1001
Age	21
Type of Contact	Self Enquiry
City Tier	3
Duration of Pitch	2.0
Occupation	Free Lancer
Gender	Male
Number of Person Visiting	1
Number of Followups	0
Product Pitched	Basic
Preferred Property Star	1
Marital Status	Unmarried
Number of Trips	1
Passport	No (0)
Pitch Satisfaction Score	1
Own Car	No (0)
Number of Children Visiting	0
Designation	Executive
Monthly Income	8000
Total Visiting	1

Expected Result:

Prediction: Will Not Buy Product


📁 Project Structure

travel-purchase-predictor/
│
├── app.py
├── rf_model.pkl
├── preprocessor.pkl
├── requirements.txt
├── README.md
└── templates/
    └── index.html

    
📊 Model Info
The model is trained using:

Classification algorithm: Random Forest

Target variable: ProdTaken (0 or 1)

Input features: Encoded from form (categorical and numerical)


📬 Contact
For any queries or suggestions, feel free to connect:

Aryan Patel

Email: [aryanpatel77462.com]
