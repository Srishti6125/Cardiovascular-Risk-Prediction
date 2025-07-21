# 🩺 CHD Prediction Using Machine Learning

> Predicting Coronary Heart Disease (CHD) using supervised learning models, hyperparameter tuning, and model explainability techniques like SHAP.

---

## 🧠 Problem Statement

The goal of this project is to predict whether an individual is at risk of developing Coronary Heart Disease (CHD) in the next 10 years based on health and lifestyle factors. Accurate early prediction can help initiate timely medical interventions and improve quality of life.

---

## 📦 Dataset

- **Source**: [(https://drive.google.com/drive/folders/1SioMV4Q4MpHl0xvFInrRDvXv29fBgJ4m)]
- **Target Variable**: `TenYearCHD`
- **Features Used**: Age, sex, systolic BP, diastolic BP, cholesterol levels, smoking status, diabetes, etc.

---

## 🔧 Tech Stack

| Task | Tools/Libraries |
|------|-----------------|
| Data Analysis | `Pandas`, `NumPy`, `Matplotlib`, `Seaborn`, `Plotly` |
| Modeling | `Scikit-learn`, `Logistic Regression`, `Random Forest`, `XGBoost`, `Decision Tree` |
| Tuning | `GridSearchCV` |
| Explainability | `SHAP` |
| IDE | Google Colab / Jupyter Notebook |

---

## 🔄 Project Workflow

```
📁 Load and Explore Dataset
🧼 Handle Missing Values
📊 Exploratory Data Analysis (EDA)
🧪 Feature Selection and Scaling
🤖 ML Model Implementation:
   - Logistic Regression
   - Decision Tree
   - Random Forest
   - XGBoost
🎯 Model Evaluation (Precision, Recall, F1, ROC AUC)
🔍 Hyperparameter Tuning (GridSearchCV)
🧠 SHAP Explainability and Visualization (Plotly)
📈 Final Model Selection & Interpretation'
```

---

## 📌 Key Takeaways

- Decision Tree showed the best recall, ensuring more at-risk patients were identified.
- SHAP values highlighted top risk factors like age, systolic BP, and diabetes.
- The project showed how explainable ML can be applied to healthcare for actionable insights.

---
