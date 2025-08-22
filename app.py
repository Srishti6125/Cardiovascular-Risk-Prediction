from flask import Flask, render_template, request 
import joblib
import numpy as np 

app = Flask(__name__) 

MODEL_PATH = 'cardio_risk_model.joblib' 
model = joblib.load(MODEL_PATH)
scaler = joblib.load('scaler.joblib')
    
# --- Helpers --- 
def to_float(v, default=0.0): 
    try: 
        return float(v) 
    except Exception: 
        return float(default) 
    
def checkbox_to_num(val):
    return 1 if val == "1" else 0

@app.route('/') 
def index(): 
    return render_template('index.html') 

@app.route('/predict', methods=['POST']) 
def predict(): 
    prediction_text = None
    advice = ''
    risk_category = ''
    risk_level = ''
    filled = dict(request.form)  # For form stickiness on full reload

    try: 
        # --- Collect form data --- 
        age = to_float(request.form.get('age')) 
        education = request.form.get('education') # collected but not used 
        sex = request.form.get('sex') # collected but not used 
        # Smoking 
        is_smoking = request.form.get('is_smoking') 
        cigsPerDay = to_float(request.form.get('cigsPerDay')) if is_smoking == "1" else 0
        
        # Medical features 
        BPMeds = checkbox_to_num(request.form.get('BPMeds')) 
        prevalentStroke = checkbox_to_num(request.form.get('prevalentStroke')) 
        prevalentHyp = checkbox_to_num(request.form.get('prevalentHyp')) 
        diabetes = checkbox_to_num(request.form.get('diabetes')) 
        
        # Numeric features 
        totChol = to_float(request.form.get('totChol')) 
        sysBP = to_float(request.form.get('sysBP')) 
        diaBP = to_float(request.form.get('diaBP')) 
        BMI = to_float(request.form.get('BMI')) 
        heartRate = to_float(request.form.get('heartRate')) 
        glucose = to_float(request.form.get('glucose')) 
        
        # Derived feature 
        pulse_pressure = sysBP - diaBP 
        
        # Final feature vector (11 only) 
        features = [ age, pulse_pressure, prevalentHyp, diabetes, totChol, BPMeds, glucose, prevalentStroke, cigsPerDay, BMI, heartRate ] 
        
        print("Features sent to model:", features)  # <-- Add this line

         # Scale features before prediction
        features_scaled = scaler.transform([features])
        print("Scaled features sent to model:", features_scaled)  # Optional debug

        # Prediction 
        prediction = model.predict_proba(features_scaled)[0][1] 
        print("Model prediction (probability):", prediction)  # <-- Add this line

        risk_score = round(prediction * 100, 2) 

        # Risk categorization 
        if risk_score < 30: 
            risk_category = "Low Risk" 
            advice = "✅ Maintain a healthy lifestyle with regular exercise and balanced diet." 
        elif 30 <= risk_score < 60: 
            risk_category = "Moderate Risk" 
            advice = "⚠️ Consider lifestyle adjustments and regular checkups." 
        else: 
            risk_category = "High Risk" 
            advice = "🚨 Seek medical consultation and adopt strict lifestyle modifications." 
        
        risk_level = risk_category.split()[0].lower()  # e.g., "low", "moderate", "high" for CSS class
        
        prediction_text = f"Predicted Risk: {risk_score:.2f}% ({risk_category})"
    
    except Exception as e: 
        prediction_text = f"Error: {str(e)}"
    
    return render_template( 
        'index.html', 
        prediction_text=prediction_text, 
        advice=advice,
        risk_category=risk_category,
        risk_level=risk_level,
        filled=filled
    ) 
    
if __name__ == '__main__': 
    app.run(debug=True)
