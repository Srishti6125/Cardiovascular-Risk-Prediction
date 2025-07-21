# 🩺 CHD Prediction Using Machine Learning

> Predicting Coronary Heart Disease (CHD) using supervised learning models, hyperparameter tuning, and model explainability techniques like SHAP.

---

## 🧠 Problem Statement

The goal of this project is to predict whether an individual is at risk of developing Coronary Heart Disease (CHD) in the next 10 years based on health and lifestyle factors. Accurate early prediction can help initiate timely medical interventions and improve quality of life.

---

## 📦 Dataset

- **Source**: [Risk Prediction dataset](https://drive.google.com/drive/folders/1SioMV4Q4MpHl0xvFInrRDvXv29fBgJ4m)
- **Target Variable**: `TenYearCHD`
- **Features Used**: `age`, `education `, `sex`, `is_smoking`, `cigsPerDay`, `BPMeds`, `prevalentStroke`, `prevalentHyp`, `diabetes`, `totChol`, `sysBP`, `diaBP`, `BMI`, `heartRate`, `glucose`

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

## ✅ Model Comparison

| Model              | Accuracy | Precision | Recall | F1-Score | ROC AUC |
|-------------------|----------|-----------|--------|----------|---------|
| Logistic Regression | 69.1%   | 0.27      | 0.69   | 0.39     | 0.69    |
| Random Forest       | 74.4%   | 0.27      | 0.46   | 0.34     | 0.62    |
| XGBoost             | 74.2%   | 0.25      | 0.43   | 0.32     | 0.61    |
| **Decision Tree (Tuned)** ✅ | **67.4%**   | **0.23**      | **0.55**   | **0.32**     | **0.62**    |

---

## 💡 Final Model: Decision Tree (Tuned)

- Chosen for its **high recall**, which is critical in medical applications where it's more important to **flag potential CHD cases**, even at the cost of a few false positives.
- Offers **model interpretability** through feature importance and SHAP plots, ideal for healthcare explainability.

---

## 📊 SHAP Explainability

Using SHAP, the most important features influencing the model's decisions were:

- **Age**
- **Cigarettes Per Day**
- **Systolic BP**

Visualized using an interactive Plotly bar chart.

---

## 📌 Key Takeaways

- Decision Tree showed the best recall, ensuring more at-risk patients were identified.
- SHAP values highlighted top risk factors like age, systolic BP, and diabetes.
- The project showed how explainable ML can be applied to healthcare for actionable insights.

---
