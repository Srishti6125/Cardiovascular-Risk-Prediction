from flask import Flask, render_template, request
from joblib import load
import numpy as np

app = Flask(__name__)

# Load the saved model
model = load("cardio_risk_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)[0]
    result = "CHD Risk Present" if prediction == 1 else "No CHD Risk"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
