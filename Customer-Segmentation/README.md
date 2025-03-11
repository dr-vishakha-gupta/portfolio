# 🎯 Customer Segmentation Using Machine Learning  

## 🚀 Project Overview  
Customer segmentation is a key strategy for businesses to **personalize marketing efforts, improve customer engagement, and optimize resource allocation**.  
This project applies **unsupervised learning (K-Means Clustering)** to segment customers based on their spending patterns and demographics, providing actionable insights for marketing teams.  

## 📌 Business Problem  
A retail company wants to improve its **customer targeting strategy** by segmenting customers based on purchasing habits.  
The goal is to:  
✔️ **Identify key customer segments** for personalized marketing.  
✔️ **Increase sales conversions** by targeting the right audience.  
✔️ **Optimize resource allocation** to avoid unnecessary ad spending.  

---

## **🛠️ Solution Approach**  

### **🔍 1. Data Understanding & Preprocessing**  
- Data cleaning (handling missing values, duplicates, and outliers).  
- Exploratory Data Analysis (**EDA**) to identify patterns in customer behavior.  
- Normalizing and scaling data for better clustering results.  

### **📊 2. Exploratory Data Analysis (EDA) & Feature Engineering**  
- Analyzing customer attributes (**Age, Income, Spending Score, Frequency of Purchases**).  
- Visualizing patterns using **Seaborn & Matplotlib**.  
- Selecting relevant features for clustering.  

### **🤖 3. Machine Learning Model - K-Means Clustering**  
- **Elbow Method** to determine the optimal number of clusters.  
- Applying **K-Means Algorithm** to segment customers.  
- Evaluating clustering performance using the **Silhouette Score**.  

---

## **📈 Visualizations & Insights**  

### **📌 Elbow Method for Optimal Clusters**  
The **Elbow Method** is used to determine the best number of clusters by finding the point where the Within-Cluster Sum of Squares (WCSS) starts decreasing at a slower rate.  

📌 **Optimal Number of Clusters Found: 3
![Elbow Curve](Customer-Segmentation/elbow_curve.png)  

### **📌 Customer Segments Visualized**  
Here’s how customers are grouped based on their spending behavior:  

![Cluster Segmentation](Customer-Segmentation/cluster_visualization.png)  

---

## **📊 Key Business Findings & Recommendations**  
📌 **Segment 1: High-Value Customers** → Offer premium services & loyalty programs.  
📌 **Segment 2: Budget-Conscious Shoppers** → Focus on discounts & seasonal promotions.  
📌 **Segment 3: Impulse Buyers** → Engage with limited-time offers & flash sales.  

---

## **📂 Project Structure**  
