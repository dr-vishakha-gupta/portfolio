# 🎯 A/B Testing for Ad Performance Optimization  

## 📌 Project Overview  
In this project, we leverage **A/B testing and statistical hypothesis testing** to analyze **advertisement performance** and uncover actionable insights. By examining key variables such as **day of the week, time of day, and total ad displays**, we determine their impact on **conversion rates**.  

The methodology combines **exploratory data analysis (EDA)** with **rigorous statistical tests**, including:  
- **Chi-Squared Test of Independence** to evaluate relationships between categorical variables.  
- **Mann-Whitney U Test** to compare distributions of a continuous variable across conversion groups.  

This analysis enables **data-driven decision-making** for optimizing ad performance and increasing conversions.  

---

## 🛠 **Tools & Technologies**  
✅ **Programming:** Python (Pandas, NumPy, SciPy, Matplotlib, Seaborn)  
✅ **Statistical Testing:** Chi-Squared Test, Mann-Whitney U Test  
✅ **Visualization:** Stacked Bar Charts, Box Plots, Pie Charts  

---

## 🔍 **Exploratory Data Analysis (EDA)**  

### **1️⃣ Understanding Ad Display Trends**  
We analyze:  
✔ **Which day of the week has the highest ad displays?**  
✔ **Which hour of the day sees the most ad impressions?**  
✔ **Total number of ads shown to prospects.**  

🖼 **Ad Displays Over Time:**  
![Ad Displays Over Time](https://github.com/dr-vishakha-gupta/portfolio/blob/main/AB_Testing_Ad_Optimization/Most%20ads-%20day.png)  

(https://github.com/dr-vishakha-gupta/portfolio/blob/main/AB_Testing_Ad_Optimization/Most%20ads-%20Hour%20of%20day.png)

---

### **2️⃣ Conversion Analysis & Visualization**  
To identify meaningful patterns, we compare **conversion rates** against:  
✔ **Days of the week** (Do weekends have higher conversions?)  
✔ **Hours of the day** (Is there a peak conversion hour?)  
✔ **Total ad displays** (Is there an optimal number of exposures?)  

We use **stacked bar charts, pie charts, and box plots** to visualize these relationships.  

🖼 **Conversion Rate by Day of the Week:**  
![Conversion Rate by Day](INSERT_IMAGE_LINK_HERE)  

🖼 **Box Plot: Total Ad Displays vs. Conversion Status**  
![Box Plot](INSERT_IMAGE_LINK_HERE)  

---

## 📊 **Statistical Hypothesis Testing**  

### **1️⃣ Chi-Squared Test of Independence**  
We assess whether **categorical variables (e.g., day of the week, time of day)** significantly impact conversion rates.  

📌 **Null Hypothesis (H₀):** *There is no relationship between ad display day/time and conversion status.*  
📌 **Alternative Hypothesis (H₁):** *There is a significant relationship between these variables.*  

🖼 **Chi-Squared Test Results:**  
![Chi-Square Results](INSERT_IMAGE_LINK_HERE)  

---

### **2️⃣ Mann-Whitney U Test**  
For **continuous variables** like **total ad displays**, we check if distributions **differ significantly** between converted and non-converted groups.  

📌 **Null Hypothesis (H₀):** *The distribution of ad exposures is the same for both groups.*  
📌 **Alternative Hypothesis (H₁):** *The distribution differs significantly between converted and non-converted users.*  

🖼 **Mann-Whitney U Test Results:**  
![Mann-Whitney U](INSERT_IMAGE_LINK_HERE)  

---

## 🎯 **Key Insights & Business Impact**  
✔ **Ad Timing Matters:** Certain hours of the day **show significantly higher conversion rates**.  
✔ **Day of the Week is a Key Factor:** Weekends may have a different **ad engagement pattern** than weekdays.  
✔ **Ad Exposure is Non-Linear:** More ads **don’t always lead to more conversions**—an optimal threshold exists.  
✔ **Statistically Significant Relationships Found:** Chi-Squared and Mann-Whitney U tests confirm **data-driven ad strategy improvements**.  

---

## 🚀 **Recommendations for Ad Optimization**  
🔹 **Adjust Ad Scheduling:** Focus ad displays on **high-conversion time slots**.  
🔹 **Segment Audiences by Day:** Tailor ad creatives or promotions for **weekdays vs. weekends**.  
🔹 **Optimize Ad Frequency:** Avoid **overexposure** by determining the optimal number of impressions.  
🔹 **Run Further Experiments:** Test new ad variations using **multivariate A/B testing** for deeper insights.
