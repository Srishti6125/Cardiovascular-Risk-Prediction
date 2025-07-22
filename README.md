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
| Data Analysis | `Pandas`, `NumPy` |
| Visualization | `Matplotlib`, `Seaborn`, `Plotly` |
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

| Model                     | Accuracy | Precision | Recall | F1 Score | ROC AUC |
|--------------------------|----------|-----------|--------|----------|---------|
| Logistic Regression       | 65.5%    | 62.5%     | 68.9%  | 65.6%    | 65.6%   |
| Logistic Regression (Tuned) | 64.8% | 61.2%     | 72.0%  | 66.2%    | 65.2%   |
| Decision Tree             | 68.5%    | 68.9%     | 61.8%  | 65.2%    | 68.2%   |
| Decision Tree (Tuned)     | 73.6%    | 73.8%     | 69.3%  | 71.5%    | 73.4%   |
| Random Forest (Tuned)     | 84.2%    | 81.3%     | 86.9%  | 84.0%    | 84.3%   |
| XGBoost                   | 80.8%    | 79.1%     | 81.3%  | 80.2%    | 80.8%   |
| **XGBoost (Tuned)** ✅     | **88.5%**| **87.6%** | **88.5%** | **88.1%** | **88.5%** |

---

## 💡 Final Model: Tuned XGBoost

The tuned XGBoost classifier was selected as the final model due to its outstanding performance across all evaluation metrics. It provided the best balance of precision and recall, minimized false negatives (which is crucial in healthcare), and showed excellent generalization with a testing accuracy of **88.5%** and F1 score of **88.1%**.

---


## 📊 SHAP Explainability

To interpret the model's predictions, **SHAP (SHapley Additive Explanations)** was used. It revealed the most influential features contributing to CHD risk:

- **Age**
- **Education**
- **Cigarettes per Day**
- **heartrate**
- **Systolic Blood Pressure (sysBP)**

These were visualized using an interactive Plotly bar chart to enhance model transparency and explainability.

---


## 📌 Key Takeaways

This project demonstrates how machine learning can be effectively applied to healthcare data to predict CHD risk. The tuned XGBoost model delivered the best performance, with high recall and model interpretability via SHAP. Crucial clinical features such as age, systolic blood pressure, glucose levels, and smoking habits were identified as key predictors of CHD. With both accuracy and explainability, the final model is suitable for real-world medical decision support systems.

---
