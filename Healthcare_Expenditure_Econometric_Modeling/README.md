# 📊 Macroeconomic Determinants of Healthcare Expenditures: An Econometric Approach  
*A Regime-Switching & Non-Linear Econometric Analysis of Healthcare Spending*  

---

🖼 **PCE-Health Spending Over Time:**  
![PCE Health](https://github.com/dr-vishakha-gupta/portfolio/blob/main/Healthcare_Econometric_Modeling/PCE-Health.png) 

## 🔍 Project Overview  
Healthcare spending is a crucial component of economic policy, but its behavior is often **non-linear and regime-dependent** due to **inflation, monetary policy, and macroeconomic shocks** (e.g., recessions, pandemics).  

This study employs **advanced econometric modeling** to analyze **how healthcare expenditures respond to macroeconomic variables across different economic regimes** using:  

✔ **Markov Switching Models (MSM)** – To identify **structural shifts and regime-dependent relationships**.  
✔ **Impulse Indicator Saturation (IIS) & Step Indicator Saturation (SIS)** – To detect **structural breaks and sudden shocks** in expenditure patterns.  
✔ **Non-Linear Autometrics & Bias-Corrected Estimators** – To assess **asymmetric effects of inflation, monetary policy, and crises on healthcare spending**.  
✔ **Error Correction Modeling (ECM) & Cointegration Analysis** – To differentiate **short-term fluctuations from long-run equilibrium trends**.  

📢 **Key Question:** *How do monetary policy, inflation, and economic shocks influence healthcare spending in stable vs. volatile economic regimes?*  

---

## 🏗 Methodology & Econometric Models  

### **1️⃣ Linear Model: Benchmark Regression (OLS & Autometrics Selection)**  
We start with a **baseline Ordinary Least Squares (OLS) model**, followed by **Autometrics selection (Impulse Indicator Saturation & Step Indicator Saturation - IIS/SIS)** to detect:  

✔ **Sudden shocks** (e.g., financial crises, pandemics, major policy changes).  
✔ **Long-term structural shifts** (e.g., demographic changes, healthcare reforms).  

🖼 **Structural Breaks Detected in Healthcare Spending:**  
![Structural Breaks](https://github.com/dr-vishakha-gupta/portfolio/blob/main/Healthcare_Econometric_Modeling/StructuralBreaks.png)  

---

### **2️⃣ Markov-Switching Model (Regime-Dependent Analysis)**  
Since healthcare spending is **regime-dependent**, a **Markov-Switching Model (MSM)** is used to analyze how macroeconomic factors impact spending **in stable vs. volatile economic periods**.  

🖼 **Markov-Switching Estimates Plot:**  
![Markov Switching](https://github.com/dr-vishakha-gupta/portfolio/blob/main/Healthcare_Econometric_Modeling/MarkovSwitching.png)  

📌 **Two Distinct Economic Regimes Identified:**  
- **Regime 0 (Stable Growth Phase)**:  
  - Healthcare inflation **(Medical CPI)** is the **dominant driver** of spending (β=0.565).  
  - **Federal Funds Rate (Monetary Policy)** has **no significant impact**.  
- **Regime 1 (Economic Stress/Volatility Phase)**:  
  - **FEDFUNDS becomes significant (p=0.009),** meaning monetary policy affects healthcare spending **only during crisis periods**.  
  - **Epidemic Indicator becomes significant (p=0.018),** showing that **health crises drive spending surges**.  
  - The effect of **Medical CPI weakens** (β=0.195), meaning **inflation is less impactful during crises than in stable periods**.  

---

### **3️⃣ Non-Linear Relationships & Bias Correction**  
A **generalized non-linear regression model** is applied to evaluate **asymmetric effects of macroeconomic variables**:  

🖼 **Non-Linear CPI Impact on Spending:**  
![Non-Linear CPI](https://github.com/dr-vishakha-gupta/portfolio/blob/main/Healthcare_Econometric_Modeling/NonLinearPlot.png)  

📌 **Findings:**  
✔ **Monetary policy’s effect is asymmetric** – It **only influences spending during recessions**.  
✔ **Epidemics create a structural break**, meaning **healthcare spending surges independently of inflationary trends**.  

---

### **4️⃣ Residual Diagnostics & Model Fit**  
To assess model performance, we evaluate:  
✔ **Log-Likelihood: 950.39** (Strong model fit).  
✔ **R²: 91%** (Explains **91% of healthcare spending variation**).  
✔ **Linearity Test (p < 0.0001):** Strong rejection of linearity, justifying **Markov-Switching approach**.    

🖼 **Residual Analysis & Model Fit:**  
![Residual Fit](https://github.com/dr-vishakha-gupta/portfolio/blob/main/Healthcare_Econometric_Modeling/ResidualFit.png)  

---

## 📂 Data Sources & Description  
This study utilizes **seasonally adjusted quarterly data** from **1971 to 2024**, sourced from:  
- **Federal Reserve Economic Data (FRED)** – Macroeconomic indicators.  
- **Bureau of Economic Analysis (BEA)** – **Personal Consumption Expenditures on Healthcare (PCE-Health)**.  
- **National Bureau of Economic Research (NBER)** – Recession and expansion periods.  

### **Dependent Variable:**  
- **PCE-Health**: *Personal Consumption Expenditures on Healthcare (billions, real USD).*   

### **Key Independent Variables:**  
| Variable | Description | Expected Effect |
|----------|------------|----------------|
| **FEDFUNDS** | Federal Funds Rate (Monetary Policy) | **(-)** High rates may reduce spending. |
| **DLCPIMEDSL** | Medical CPI (Inflation in healthcare sector) | **(+)** Rising costs may increase spending. |
| **GDP Growth** | % change in real GDP | **(+)** Economic expansion supports healthcare demand. |
| **Unemployment Rate** | Labor market condition indicator | **(-)** Higher unemployment may reduce affordability. |
| **Epidemic Indicator** | Dummy variable for major health crises (e.g., COVID-19, H1N1) | **(+)** Health crises drive emergency healthcare spending. |

---

## 📌 **Policy Implications & Recommendations**  

✔ **Healthcare inflation is the dominant driver of long-run expenditures,** but its impact weakens in downturns.  
✔ **Monetary policy (FEDFUNDS) only matters during economic distress**, suggesting policymakers should **avoid aggressive tightening during downturns**.  
✔ **Health crises (e.g., COVID-19) create structural spending shocks**, requiring **contingency budget planning**.  
✔ **Regime-Specific Forecasting Models are necessary** to incorporate economic shifts into spending forecasts.  
