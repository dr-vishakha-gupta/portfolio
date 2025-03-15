# 🚴 London Bike Rides - Data Analysis & Visualization  

## 📌 Project Overview  
This project analyzes **London’s bike-sharing system** to uncover trends, evaluate weather impact, and optimize urban mobility strategies. Using **Python** for data exploration and **Tableau** for visualization, we extract insights that can inform city planning and bike-sharing operations.  

🔗 **[Explore the Interactive Tableau Dashboard Here](https://public.tableau.com/app/profile/vishakha.gupta6103/viz/LondonBikeRides-MovingAverageandHeatmap_17420715356660/Dashboard?publish=yes)**  

---

## 🎯 Project Goals  
- **Identify usage patterns**: Understand how bike rides fluctuate across different time periods.  
- **Analyze weather impact**: Examine how temperature and wind speed affect bike demand.  
- **Enable data-driven decision-making**: Provide insights for optimizing fleet management and user engagement.  

---

## 🛠️ Tools & Technologies  
✅ **Python**: Pandas, Matplotlib, Seaborn for data preprocessing & EDA.  
✅ **Tableau**: Interactive dashboard for trend visualization.  

---

## 📊 Data Analysis & Key Insights  

### 🔹 1. Seasonal & Daily Trends  
- Bike usage exhibits a **strong seasonal pattern**, with peak rides in warmer months (June – September) and a **sharp decline in winter** (December – February).  
- **Weekdays vs. Weekends**: Weekday rides are **more structured**, likely driven by commuting, while weekends show more **sporadic** usage.  
- **Drop in late autumn (October–November)**: Possibly due to reduced daylight and worsening weather conditions.  

### 🔹 2. Weather Impact on Bike Usage  
- **Temperature Correlation**: Rides **increase sharply** as temperature rises, peaking around **15-20°C**. Beyond this, the increase slows down.  
- **Wind Speed Effect**:  
  - Rides **remain stable up to ~20 km/h winds**.  
  - Above 20 km/h, usage **drops significantly**, suggesting discomfort in strong winds.  
- **Cold & Windy Days = Low Demand**: The heatmap analysis confirms that fewer people ride on days when both temperature is **below 10°C** and wind speed **exceeds 30 km/h**.  

### 🔹 3. Moving Average Trends  
- The **14-day moving average** smooths fluctuations and reveals underlying trends.  
- Noticeable **dips in winter months**, but a rapid recovery in early spring.  
- A **steep decline in a specific period (October–December 2015)** suggests an external factor—possibly a temporary bike shortage or weather anomaly.  

---

## 📈 Tableau Visualization Highlights  

### 🔹 Dashboard Features  
✅ **Total Rides Counter**: Displays the total number of rides over the study period.  
✅ **Time-Series Chart**: 14-day moving average trends help in spotting seasonal shifts.  
✅ **Filter Controls**: Users can select different **timeframes & moving average periods** for customized analysis.  
✅ **Heatmap (Temperature vs. Wind Speed)**: Displays **concentration of bike rides under various weather conditions**.  

### 🔹 Business Implications  
- **Dynamic Bike Allocation**: More bikes should be deployed **during summer months and weekdays**.  
- **Weather-Responsive Pricing**: Offer **discounts or promotions on cold & windy days** to maintain ridership.  
- **Infrastructure Planning**: Install **bike shelters in high-wind areas** to encourage year-round usage.  
- **Predictive Maintenance**: Based on ride trends, schedule maintenance **before peak seasons** to avoid disruptions.  
