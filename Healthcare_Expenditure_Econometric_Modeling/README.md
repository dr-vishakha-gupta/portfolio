# 📊 Macroeconomic Determinants of Healthcare Expenditures: An Econometric Approach  
*A Regime-Switching & Non-Linear Econometric Analysis of Healthcare Spending*  

## 🔍 Project Overview  
This project investigates the **macroeconomic determinants of healthcare expenditures** using advanced **econometric modeling techniques**, including:  

- **Markov Switching Models (MSM)** to capture **structural shifts and economic regimes** affecting healthcare spending.  
- **Impulse Indicator Saturation (IIS) & Step Indicator Saturation (SIS)** for detecting **outliers and structural breaks** in expenditure trends.  
- **Non-Linear Autometrics & Bias-Corrected Estimators** to assess **asymmetric and time-varying effects** of inflation, monetary policy, and economic crises on healthcare spending.  
- **Error Correction Modeling (ECM) & Cointegration Analysis** to distinguish **short-term fluctuations** from **long-run equilibrium relationships** between healthcare spending and macroeconomic variables.  

This study aims to **provide a robust empirical framework for understanding how economic conditions shape healthcare expenditures** and inform **policy-making, budget allocation, and financial planning** in the healthcare sector.  

---

## 🎯 Objectives  
- **Examine the dynamic evolution of healthcare expenditures (PCE-Health) from 1971 to 2024 using quarterly data.**  
- **Identify regime shifts in healthcare spending behavior** using a **Markov-Switching approach**.  
- **Investigate the role of monetary policy, inflation, and economic shocks** in driving healthcare consumption patterns.  
- **Test for non-linearities and asymmetric responses** in healthcare spending during economic expansions vs. contractions.  
- **Provide actionable policy recommendations** based on empirical findings.  

---

## 📂 Data Sources & Description  
This study utilizes **seasonally adjusted quarterly data** from **1971 to 2024**, sourced from:  
- **Federal Reserve Economic Data (FRED)** for macroeconomic indicators.  
- **Bureau of Economic Analysis (BEA)** for **Personal Consumption Expenditures on Healthcare (PCE-Health)**.  
- **National Bureau of Economic Research (NBER)** for recession and expansion periods.  

### **Dependent Variable:**  
- **PCE-Health**: *Personal Consumption Expenditures on Healthcare (billions, real USD).*
![PCE Health](https://github.com/dr-vishakha-gupta/portfolio/blob/main/Healthcare_Expenditure_Econometric_Modeling/PCE-Health.png)  

### **Key Independent Variables:**  
| Variable | Description | Expected Effect |
|----------|------------|----------------|
| **FEDFUNDS** | Federal Funds Rate (Monetary Policy) | **(-)** High rates may reduce spending. |
| **DLCPIMEDSL** | Medical CPI (Inflation in healthcare sector) | **(+)** Rising costs may increase spending. |
| **GDP Growth** | % change in real GDP | **(+)** Economic expansion supports healthcare demand. |
| **Unemployment Rate** | Labor market condition indicator | **(-)** Higher unemployment may reduce affordability. |
| **Epidemic Indicator** | Dummy variable for major health crises (e.g., COVID-19, H1N1) | **(+)** Health crises drive emergency healthcare spending. |

---

## 🏗 **Methodology & Econometric Models**  

### **1️⃣ Linear Model: Benchmark Regression (OLS & Autometrics Selection)**  
We begin with a **baseline Ordinary Least Squares (OLS) model**, followed by **Autometrics selection (Impulse Indicator Saturation & Step Indicator Saturation - IIS/SIS)** to detect **outliers and structural breaks**.  

- **IIS captures sudden economic shocks (financial crises, pandemics, policy shifts).**  
- **SIS identifies persistent shifts (new economic policies, demographic changes).**  

🖼 **Structural Breaks Detected in Healthcare Spending:**  
![Structural Breaks](https://github.com/dr-vishakha-gupta/portfolio/blob/main/Healthcare_Expenditure_Econometric_Modeling/StructuralBreaks.png)  

---

### **2️⃣ Markov-Switching Model (Regime-Dependent Analysis)**  
Given **non-stationary and regime-dependent shifts in healthcare expenditures**, a **Markov-Switching Model (MSM)** is implemented:  

🖼 **Markov-Switching Estimates Plot:**  
![Markov Switching](https://github.com/dr-vishakha-gupta/portfolio/blob/main/Healthcare_Expenditure_Econometric_Modeling/MarkovSwitching.png) 

📌 **Two Distinct Economic Regimes Identified:**  
- **Regime 0 (Stable Growth Phase)**:  
  - Healthcare inflation **(Medical CPI)** is the **dominant driver** of spending (β=0.565).  
  - **Federal Funds Rate (Monetary Policy)** has **no significant impact**.  
- **Regime 1 (Economic Stress/Volatility Phase)**:  
  - **FEDFUNDS becomes significant (p=0.009),** meaning monetary policy affects healthcare spending **during crisis periods**.  
  - **Epidemic Indicator becomes significant (p=0.018),** showing that **health shocks drive spending surges.**  
  - The effect of **Medical CPI weakens** (β=0.195), meaning inflation is less impactful in crises than in stable periods.  

---

### **3️⃣ Non-Linear Relationships & Bias Correction**  
A **generalized non-linear regression model** is applied to evaluate **asymmetric effects of macroeconomic variables**:  

🖼 **Non-Linear CPI Impact on Spending:**  
![Non-Linear CPI]((https://github.com/dr-vishakha-gupta/portfolio/blob/main/Healthcare_Expenditure_Econometric_Modeling/NonLinearPlot.png)  

---

### **4️⃣ Residual Diagnostics & Model Fit**  
To assess model performance, we evaluate:  
✔ **Log-Likelihood: 950.39** (Strong model fit)  
✔ **R²: 91%** (Explains 91% of healthcare spending variation)  
✔ **Linearity Test (p < 0.0001):** Strong rejection of linearity, justifying **Markov-Switching approach**.    

---

## 📌 **Key Policy Implications**  

✔ **Healthcare inflation is the dominant driver of long-run expenditures,** but its impact weakens in downturns.  
✔ **Monetary policy (FEDFUNDS) only matters during economic distress**, suggesting policymakers should **avoid aggressive tightening during downturns**.  
✔ **Health crises (e.g., COVID-19) create structural spending shocks**, requiring **contingency budget planning**.  
✔ **Regime-Specific Forecasting Models are necessary** to incorporate economic shifts into spending forecasts.  
