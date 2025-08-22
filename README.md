# 🩺 CHD Prediction Using Machine Learning + Flask Web App

> Predicting Coronary Heart Disease (CHD) using supervised learning models, hyperparameter tuning, model explainability (SHAP), and a deployed Flask web application.  

🌐 **Live App**: [Try it here!](https://cardiovascular-risk-prediction-ylna.onrender.com/)

---

## 🧠 Problem Statement

The goal of this project is to predict whether an individual is at risk of developing Coronary Heart Disease (CHD) in the next 10 years based on health and lifestyle factors.  
Accurate early prediction can help initiate timely medical interventions and improve quality of life.

---

## 📦 Dataset

- **Source**: [Risk Prediction dataset](https://drive.google.com/drive/folders/1SioMV4Q4MpHl0xvFInrRDvXv29fBgJ4m)  
- **Target Variable**: `TenYearCHD`  
- **Features Used**:  
  `age`, `education`, `sex`, `is_smoking`, `cigsPerDay`, `BPMeds`,  
  `prevalentStroke`, `prevalentHyp`, `diabetes`, `totChol`, `sysBP`,  
  `diaBP`, `BMI`, `heartRate`, `glucose`  

---

## 🔧 Tech Stack

| Task            | Tools/Libraries |
|-----------------|-----------------|
| Data Analysis   | `Pandas`, `NumPy` |
| Visualization   | `Matplotlib`, `Seaborn`, `Plotly` |
| Modeling        | `Scikit-learn`, `Logistic Regression`, `Random Forest`, `XGBoost`, `Decision Tree` |
| Tuning          | `GridSearchCV` |
| Explainability  | `SHAP` |
| Deployment      | `Flask`, `Render` |
| IDE             | Google Colab / Jupyter Notebook |

---

## 🔄 Project Workflow

```
📁 Load and Explore Dataset
🧼 Handle Missing Values
📊 Exploratory Data Analysis (EDA)
🧪 Feature Selection and Scaling
🤖 ML Model Implementation (Logistic Regression, Decision Tree, Random Forest, XGBoost)
🎯 Model Evaluation (Precision, Recall, F1, ROC AUC)
🔍 Hyperparameter Tuning (GridSearchCV)
🧠 SHAP Explainability and Visualization (Plotly)
📈 Final Model Selection & Interpretation
🌐 Flask App Deployment on Render
```

---


---

## 🛠️ Models Trained & Comparison

| Model                       | Accuracy | Precision | Recall | F1 Score | ROC AUC |
|-----------------------------|----------|-----------|--------|----------|---------|
| Logistic Regression         | 64.9%    | 61.9%     | 70.9%  | 66.1%    | 65.5%   |
| Logistic Regression (Tuned) | 65.3%    | 62.2%     | 71.1%  | 66.3%    | 65.5%   |
| Decision Tree               | 70.5%    | 72.9%     | 78.5%  | 75.6%    | 73.0%   |
| Decision Tree (Tuned)       | 72.0%    | 73.3%     | 84.9%  | 78.7%    | 73.0%   |
| Random Forest               | 77.2%    | 73.3%     | 82.2%  | 77.5%    | 77.4%   |
| Random Forest (Tuned)       | 81.8%    | 78.6%     | 84.9%  | 81.6%    | 81.9%   |
| XGBoost                     | 76.9%    | 74.1%     | 79.5%  | 76.7%    | 77.0%   |
| **XGBoost (Tuned)** ✅     | **88.8%**| **88.3%** | **88.2%** | **88.3%** | **88.8%** |

---

## 💡 Final Model: Tuned XGBoost

The tuned **XGBoost classifier** was selected as the final model due to its outstanding performance across all evaluation metrics.  
It provided the best balance of **precision and recall**, minimized false negatives (critical in healthcare), and showed excellent generalization.  

- ✅ **Accuracy**: 88.8%  
- ✅ **Recall**: 88.2%  

---

## 📊 SHAP Explainability

To interpret the model's predictions, **SHAP (SHapley Additive Explanations)** was used.  
Top influential features:  

- **Age**
- **Cigs per Day**
- **Heart Rate**
- **Glucose**
- **Pulse Pressure**

Visualized using **interactive Plotly bar charts** for model transparency.  

---

## 🌐 Flask Web App

A user-friendly web interface was developed using **Flask** and deployed on **Render**.  
The app allows users to input their health data and receive CHD risk predictions instantly.  

👉 **Live Demo**: [Cardiovascular Risk Prediction App](https://cardiovascular-risk-prediction-ylna.onrender.com/)

---

## 📌 Key Takeaways

- ML can effectively predict **10-year CHD risk** from health data.  
- **XGBoost (tuned)** achieved the highest performance.  
- **SHAP explainability** ensures transparency for healthcare use.  
- A **Flask app** makes the model interactive and accessible.  

---
