# GlucoGuide: Diabetes Prediction & Lifestyle Recommendation App

**GlucoGuide** is an end-to-end machine learning web application designed to predict diabetes risk based on clinical parameters and deliver personalized lifestyle recommendations. This project demonstrates the complete data science lifecycle—from exploration and preprocessing through model development and deployment—while simultaneously addressing an important public health concern.

### 🎯 Key Objectives
- Develop an accurate predictive model for diabetes risk assessment  
- Create an accessible tool for both healthcare professionals and the general public  
- Provide actionable, personalized health recommendations based on individual risk profiles  
- Demonstrate best practices in machine learning project implementation  

### 🩺 Problem Statement
Diabetes affects millions worldwide, with many cases going undiagnosed until complications arise. Early detection can significantly improve outcomes through lifestyle modifications and timely medical intervention. GlucoGuide aims to bridge this gap by providing an accessible screening tool and personalized guidance based on scientific evidence.

## 📊 Dataset Analysis & Preparation

### 📁 Data Source
The **Pima Indians Diabetes Dataset** was selected for this project due to its reliability, widespread use in medical research, and public availability. It contains records from **768 female patients** of Pima Indian heritage, providing a focused demographic sample with established diabetes prevalence.

### 🔍 Exploratory Data Analysis

The initial exploration revealed several insights that guided subsequent processing decisions:

- **Distribution Analysis**: Histograms revealed significant skew in features like **Insulin**, **Skin Thickness**, and **Glucose**, indicating outliers and data quality issues.
- **Correlation Assessment**: Heatmaps showed **Glucose (0.47)**, **BMI (0.29)**, and **Age (0.24)** as top predictors.
- **Missing Value Investigation**: Zero values were treated as missing in features like **Glucose**, **Blood Pressure**, **BMI**, **Insulin**, and **Skin Thickness**.
- **Class Imbalance**: Target class distribution was ~65% non-diabetic vs. 35% diabetic.
- **Pair Plot Analysis**: Showed clear class separability across **Glucose**, **BMI**, and **Age**.

### 🧹 Data Preprocessing Pipeline

#### 🔻 Missing Value Treatment
- Replaced biologically implausible zero values with `NaN` in **Glucose**, **Blood Pressure**, **BMI**, **Skin Thickness**, and **Insulin**
- Used **KNN Imputer (k=5)** to fill in missing values based on similar patient profiles

#### 📏 Feature Scaling
- Applied **StandardScaler** to normalize all numerical features (mean = 0, std = 1)

#### 📊 Feature Engineering
While we explored advanced feature engineering, we proceeded with original features due to dataset size and clarity. No additional features were engineered in the final model pipeline to preserve model interpretability.

#### 🔀 Train-Test Split
- Used **Stratified 80-20 split** to ensure target class balance in both training and test sets
- Set **random_state=42** for reproducibility

## 🤖 Model Development & Evaluation

### ⚙️ Model Selection Strategy

We evaluated several models and finalized **CatBoost Classifier** based on performance.

#### ✅ Models Explored:
- **Logistic Regression** – Baseline model (accuracy: 76%)
- **K-Nearest Neighbors (KNN)** – Captures local patterns (accuracy: 74%)
- **Random Forest** – Handles non-linear relationships (accuracy: 81%)
- **XGBoost** – Strong performance on tabular data (accuracy: 85%)
- **CatBoost** – Final selected model (accuracy: 89%)

### 🧪 Why CatBoost?
- Outperformed other models in **precision**, **recall**, and **F1-score**
- Handles missing values internally
- Less sensitive to hyperparameter tuning
- Fast training with robust accuracy on tabular datasets

### 🎯 Hyperparameter Tuning

Used **GridSearchCV** to optimize parameters for all ensemble models.

**Final test results for CatBoost:**

| Metric     | Score |
|------------|-------|
| Accuracy   | 89%   |
| Precision  | 0.87  |
| Recall     | 0.90  |
| F1-Score   | 0.88  |
| ROC-AUC    | 0.92  |


## 📈 Feature Importance (from CatBoost)

| Feature                    | Importance (%) |
|----------------------------|----------------|
| Glucose                    | 41.3%          |
| BMI                        | 18.7%          |
| Age                        | 14.2%          |
| Diabetes Pedigree Function| 10.8%          |


## 🎯 Model Interpretation & Explainability

To ensure transparency and trust, we applied several interpretability techniques:

- **SHAP (SHapley Additive Explanations)**: Visualized contributions of individual features for single predictions  
- **Partial Dependence Plots**: Analyzed how each feature influenced predictions  
- **Feature Importance Charts**: Communicated top predictors globally  


## 🌐 Web Application Development

### 🛠️ Design Philosophy

The Streamlit web app was built with:

- Accessibility for non-technical users  
- Clarity of risk score and model logic  
- Actionability through health guidance based on inputs  

### 🧩 Key Components

#### ✅ User Interface

- Sidebar inputs for all features using sliders and number fields  
- Tooltips explaining medical context of each feature  
- Submit Button to trigger model prediction  

#### ⚙️ Backend Logic

- Input validation + transformation matching model pipeline  
- CatBoost model loaded from serialized `.cbm` file  
- Probabilistic prediction + binary classification  
- Risk level displayed with context-aware recommendations  

#### 📤 Output Features

- Risk score + diabetes prediction  
- SHAP summary for major contributing features (if enabled)  
- Tailored health suggestions (diet, lifestyle, checkups)  

## 📋 Recommendation System Logic

Used a rule-based system depending on:

- Prediction class (0 or 1)  
- Thresholds for **BMI**, **Glucose**, **Age**  
- Established medical guidelines  

### 💡 Examples:

- **High BMI** → Guidance on exercise and calorie balance  
- **High Glucose** → Low-GI diet tips and carb tracking  
- **Seniors** → Regular A1C testing and annual eye exams  


## 🚀 Deployment & Monitoring

### 🛰️ Deployment Steps

- Pushed code and model to GitHub repo  
- Hosted app using Streamlit Cloud  
- Managed dependencies with `requirements.txt`  
- Ensured reproducibility with fixed seeds and saved model state  

### 🛡️ Monitoring (Basic)

- Logged prediction flow and errors in console  
- App auto-refreshes with Streamlit for quick iteration  



## 🔮 Future Enhancements

### 🧠 Model & Data

- Integrate larger, more diverse datasets  
- Time-series tracking for risk progression  
- Add prediction for **Type 1** / **gestational diabetes**  

### 📱 App Features

- Multi-language UI  
- Mobile-friendly layout  
- Integration with **Apple Health** / **Google Fit**  

### 🧪 Clinical Validation

- Collaborate with medical experts for real-world testing  
- Compare results with **ADA** and **WHO** risk tools  

## 🤝 Ethical Considerations

- **Data Privacy**: No data is stored; all processing is client-side  
- **Disclaimer**: App supplements—not replaces—medical consultation  
- **Bias Awareness**: Acknowledge limitations due to dataset demographics (Pima Indian women)  
- **Accessibility**: Designed for users across literacy and tech skill levels  

## 📚 Technical Stack & Tools

| Area                | Tools Used                                 |
|---------------------|---------------------------------------------|
| Core Programming    | Python 3.8, Jupyter Notebook                |
| Modeling            | CatBoost 1.1.1, Scikit-learn 1.0.2          |
| Data Processing     | Pandas 1.4.2, NumPy 1.22.3                   |
| Visualization       | Matplotlib 3.5.1, Seaborn 0.11.2, Plotly 5.6.0 |
| Model Explainability| SHAP 0.40.0                                 |
| UI / Deployment     | Streamlit 1.15.0, Docker 20.10.14, GitHub   |
| Environment Mgmt    | Conda, requirements.txt                     |


## 🔍 Conclusion

**GlucoGuide** showcases how data science and machine learning can contribute meaningfully to public health. By delivering a robust, explainable model and pairing it with a user-centric interface, the project provides both predictive insights and actionable advice—empowering users to take proactive steps toward managing their health.
