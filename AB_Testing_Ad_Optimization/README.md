# 🎯 A/B Testing for Ad Performance Optimization  

## 📌 Project Overview  
In this project, we leverage **A/B testing and statistical hypothesis testing** to analyze **advertisement performance** and uncover actionable insights. By examining key variables such as **day of the week, time of day, and total ad displays**, we determine their impact on **conversion rates**.  

The methodology combines **exploratory data analysis (EDA)** with **rigorous statistical tests**, including:  
- **Chi-Squared Test of Independence** to evaluate relationships between categorical variables.  
- **Mann-Whitney U Test** to compare distributions of a continuous variable across conversion groups.  

This analysis enables **data-driven decision-making** for optimizing ad performance and increasing conversions.  

## 🛠 **Tools & Technologies**  
✅ **Programming:** Python (Pandas, NumPy, SciPy, Matplotlib, Seaborn)  
✅ **Statistical Testing:** Chi-Squared Test, Mann-Whitney U Test  
✅ **Visualization:** Stacked Bar Charts, Box Plots, Pie Charts  

## 🔍 **Exploratory Data Analysis (EDA)**  

### **1️⃣ Understanding Ad Display Trends**  
We analyze:  
✔ **Which day of the week has the highest ad displays?**  
✔ **Which hour of the day sees the most ad impressions?**  
✔ **Total number of ads shown to prospects.**  

🖼 **Ad Displays Over Time:**  
![Ad Displays Over Time](https://github.com/dr-vishakha-gupta/portfolio/blob/main/AB_Testing_Ad_Optimization/Most%20ads-%20day.png)  

🖼 **Most Ads - Hour of Day:**  
![Most Ads - Hour of Day](https://github.com/dr-vishakha-gupta/portfolio/blob/main/AB_Testing_Ad_Optimization/Most%20ads-%20Hour%20of%20day.png)

### **2️⃣ Conversion Analysis & Visualization**  
To identify meaningful patterns, we compare **conversion rates** against:  
✔ **Days of the week** (Do weekends have higher conversions?)  
✔ **Hours of the day** (Is there a peak conversion hour?)  
✔ **Total ad displays** (Is there an optimal number of exposures?)  

We use **stacked bar charts, pie charts, and box plots** to visualize these relationships.  

🖼 **Conversion Rate by Day of the Week:**  
![Conversion Rate by Day](https://github.com/dr-vishakha-gupta/portfolio/blob/main/AB_Testing_Ad_Optimization/Conversion%20rate%20by%20Most%20ads.png)  

🖼 **Box Plot: Total Ad Displays vs. Conversion Status**  
![Box Plot](https://github.com/dr-vishakha-gupta/portfolio/blob/main/AB_Testing_Ad_Optimization/Conversion%20Rate%20by%20test%20group.png)  


## 📊 **Statistical Hypothesis Testing**  

### **1️⃣ Chi-Square Test of Independence**  
We assess whether **categorical variables (e.g., day of the week, time of day)** significantly impact conversion rates.  

📌 **Null Hypothesis (H₀):** *There is no relationship between ad display day/time and conversion status.*  
📌 **Alternative Hypothesis (H₁):** *There is a significant relationship between these variables.*  


📊 **Test Results:**  

| **Variable**         | **Chi-Square Value** | **p-value** | **Conclusion** |
|----------------------|---------------------|-------------|---------------|
| **Test Group vs. Conversion** | 54.01 | 0.0000000000199 | ✅ Reject H₀ (Significant) |
| **Most Ads Day vs. Conversion** | 410.05 | 0.000000000000000000000000000000000193 | ✅ Reject H₀ (Significant) |
| **Most Ads Hour vs. Conversion** | 430.77 | 0.0000000000000000000000000000000000803 | ✅ Reject H₀ (Significant) |

🔍 **Interpretation:**  
✔ **Test group significantly affects conversion rates**, meaning ad variations **impact user behavior**.  
✔ **Ad display day and hour have a strong effect**, suggesting that **optimal scheduling is crucial** for conversions.  
✔ **Since all p-values are below 0.05**, we confidently **reject the null hypothesis** in all cases.  


### **2️⃣ Mann-Whitney U Test**  
For **continuous variables** like **total ad displays**, we check if distributions **differ significantly** between converted and non-converted users.  

📌 **Null Hypothesis (H₀):** *The distribution of ad exposures is the same for both groups.*  
📌 **Alternative Hypothesis (H₁):** *The distribution differs significantly between converted and non-converted users.*  

📊 **Test Results:**  

| **Metric**                | **p-value** | **Conclusion** |
|---------------------------|------------|---------------|
| **Total Ads vs. Conversion** | **0.00**   | ✅ Reject H₀ (Significant) |


🔍 **Interpretation:**  
✔ **Since the p-value is 0.00 (less than 0.05), we reject H₀**, meaning **the number of ad exposures has a significant impact on conversions**.  
✔ **More ads do not always lead to better conversions**, indicating an **optimal frequency threshold should be determined**.  


### **🚀 Business Insights & Recommendations**  
✅ **Optimize Ad Scheduling** – Since **ad display day & hour significantly affect conversions**, focus more on high-impact periods.  
✅ **Segment & Test Different Groups** – The **test group showed significant differences**, suggesting **A/B testing should be used strategically**.  
✅ **Adjust Ad Frequency** – More ads **do not always improve conversions**, meaning an **optimal ad exposure threshold should be identified**.  
