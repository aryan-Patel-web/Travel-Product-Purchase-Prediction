from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and preprocessor
model = joblib.load('rf_model.pkl')
preprocessor = joblib.load('preprocessor.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None  # Default state, nothing shown

    if request.method == 'POST':
        try:
            # Collect form inputs
            data = {
                'CustomerID': int(request.form['CustomerID']),
                'Age': float(request.form['Age']),
                'TypeofContact': request.form['TypeofContact'],
                'CityTier': int(request.form['CityTier']),
                'DurationOfPitch': float(request.form['DurationOfPitch']),
                'Occupation': request.form['Occupation'],
                'Gender': request.form['Gender'],
                'NumberOfPersonVisiting': int(request.form['NumberOfPersonVisiting']),
                'NumberOfFollowups': float(request.form['NumberOfFollowups']),
                'ProductPitched': request.form['ProductPitched'],
                'PreferredPropertyStar': int(request.form['PreferredPropertyStar']),
                'MaritalStatus': request.form['MaritalStatus'],
                'NumberOfTrips': float(request.form['NumberOfTrips']),
                'Passport': int(request.form['Passport']),
                'PitchSatisfactionScore': int(request.form['PitchSatisfactionScore']),
                'OwnCar': int(request.form['OwnCar']),
                'NumberOfChildrenVisiting': int(request.form['NumberOfChildrenVisiting']),
                'Designation': request.form['Designation'],
                'MonthlyIncome': float(request.form['MonthlyIncome']),
                'TotalVisiting': int(request.form['TotalVisiting'])
            }

            # Convert to DataFrame
            df = pd.DataFrame([data])

            # Ensure column order (if applicable)
            if hasattr(preprocessor, 'feature_names_in_'):
                df = df[preprocessor.feature_names_in_]

            # Preprocess and predict
            X = preprocessor.transform(df)
            pred = model.predict(X)[0]
            prediction = "Will Buy Product" if pred == 1 else "Will Not Buy Product"

        except Exception as e:
            prediction = f"Prediction Error: {str(e)}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
