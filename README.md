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

## 🛠️ Models Trained

| Model               | Description |
|---------------------|-------------------|
| Logistic Regression | Simple, fast, and interpretable baseline; decent calibration but limited nonlinearity handling. |
| Decision Tree       | Captures nonlinear rules and interactions; prone to overfitting without pruning. |
| Random Forest       | Strong, robust ensemble with good generalization; reduces variance and handles imbalance well. |
| XGBoost             | High-performance gradient boosting; best precision–recall/AUC after tuning in this project. |

---

## ✅ Model Comparison

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

The tuned XGBoost classifier was selected as the final model due to its outstanding performance across all evaluation metrics. It provided the best balance of precision and recall, minimized false negatives (which is crucial in healthcare), and showed excellent generalization with a testing accuracy of **88.8%** and Recall of **88.2%**.

---


## 📊 SHAP Explainability

To interpret the model's predictions, **SHAP (SHapley Additive Explanations)** was used. It revealed the most influential features contributing to CHD risk:

- **Age**
- **cigsperday**
- **heartrate**
- **glucose**
- **pulse_pressure**

These were visualized using an interactive Plotly bar chart to enhance model transparency and explainability.

---


## 📌 Key Takeaways

This project demonstrates how machine learning can be effectively applied to healthcare data to predict CHD risk. The tuned XGBoost model delivered the best performance, with high recall and model interpretability via SHAP. Crucial clinical features such as age, cigsperday, heartrate, glucose and pulse_pressure were identified as key predictors of CHD. With both accuracy and explainability, the final model is suitable for real-world medical decision support systems.

---
