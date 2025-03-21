# 🎬 Netflix SQL Analysis Project  
![Netflix Screenshot](https://github.com/dr-vishakha-gupta/portfolio/blob/main/Netflix-EDA-SQL/NetflixLogo.webp)   

## 📌 Project  
This project aims to analyze **Netflix's movie and TV show catalog** using **SQL** to uncover **key business insights**. It includes **data exploration, trend analysis, and content distribution insights** to support **data-driven decision-making**.  

---

## 🎯 Objective  
The goal of this analysis is to:  
- Perform **Exploratory Data Analysis (EDA)** on Netflix content.
- Understand **content trends** across different countries and years.  
- Identify **frequent actor pairings** and **top directors**.  
- Analyze **Netflix’s content growth strategy**.  
- Find the **highest-rated content per year**.  

---

## 🏛 Schema  
The dataset is structured as follows:  

| Column Name   | Data Type  | Description |
|--------------|-----------|-------------|
| `show_id`    | STRING    | Unique ID for each title |
| `title`      | STRING    | Name of the show or movie |
| `director`   | STRING    | Director(s) of the content |
| `casts`      | STRING    | Main actors in the content |
| `country`    | STRING    | Country of origin |
| `release_year` | INT      | Year of release |
| `rating`     | STRING    | Age rating (e.g., PG-13, TV-MA) |
| `duration`   | STRING    | Number of seasons (TV) or minutes (Movies) |
| `genre`      | STRING    | Type of content (e.g., Drama, Comedy) |

---

## 🔍 Business Problems & Solutions  

### **1️⃣ Rank the Top 5 Countries by Average Yearly Content Release**  
#### **Problem:**  
Which countries contribute the most content to Netflix over the years?  

#### **Solution Approach:**  
- Calculate the **total content** released per country **each year**.  
- Compute the **average releases per year** for each country.  
- Rank the **top 5 countries** with the highest average content releases.  

🖼 **Query Screenshot**:  
![Top Countries Query](https://github.com/dr-vishakha-gupta/portfolio/blob/main/Netflix-EDA-SQL/Top5Countries.png)  
 
📌 **Insight:**  
The **United States** and **India** are leading contributors, highlighting their dominant role in Netflix's content library.  

---

### **2️⃣ Identify the Most Frequent Actor Pairings**  
#### **Problem:**  
Which actor duos frequently appear together in Netflix content?  

#### **Solution Approach:**  
- Split the **comma-separated actor list** into **individual actor records**.  
- Find all possible actor **pairings**.  
- Count occurrences and rank the **most frequent actor pairs**.  

🖼 **Query Screenshot**:  
![Actor Pairings Query](https://github.com/dr-vishakha-gupta/portfolio/blob/main/Netflix-EDA-SQL/MostFrequentActorPair.png)  

📌 **Insight:**  
Certain actor duos appear in multiple Netflix productions, showing **strong collaborations** in the industry.  

---

### **3️⃣ Find the Longest Gap Between a Director’s Releases**  
#### **Problem:**  
Which director had the **longest time gap** between two Netflix releases?  

#### **Solution Approach:**  
- Extract **each director’s release years**.  
- Use **window functions** to calculate the **gap between consecutive releases**.  
- Find the **maximum gap** for each director and rank them.  

🖼 **Query Screenshot**:  
![TV Shows Query](https://github.com/dr-vishakha-gupta/portfolio/blob/main/Netflix-EDA-SQL/DirectorRelease.png)  

📌 **Insight:**  
Some directors take **long breaks** between projects, possibly for **high-quality production efforts** or **creative shifts**.   

---

### **4️⃣ Analyze the Growth Rate of Netflix Content Over the Years**  
#### **Problem:**  
How has Netflix’s content **expanded over time**?  

#### **Solution Approach:**  
- Count the **number of releases per year**.  
- Use **window functions** to calculate the **year-over-year growth rate**.  
- Identify **trends in Netflix's expansion strategy**.  

🖼 **Query Screenshot**:  
![Popular Genres Query](https://github.com/dr-vishakha-gupta/portfolio/blob/main/Netflix-EDA-SQL/GrowthRateNetflix.png)  

📌 **Insight:**  
Netflix saw a **major surge in content releases post-2015**, reflecting its shift towards **original content production**.  

---

### **5️⃣ Find the Highest-Rated Content Per Year**  
#### **Problem:**  
Which movie or show had the **highest rating each year**?  

#### **Solution Approach:**  
- Rank all content per year **by rating**.  
- Extract the **top-ranked** content for each year.  

🖼 **Query Screenshot**:  
![Content Trend Query](https://github.com/dr-vishakha-gupta/portfolio/blob/main/Netflix-EDA-SQL/HighestRatedContent.png)  

📌 **Insight:**  
Certain critically acclaimed shows/movies stand out **as top-rated** in their release years.  

---

## 📈 Findings  

✔ The **USA, India, and UK** have the **highest number of Netflix titles**.  
✔ **Dramas and Comedies** are the **most common genres**.  

### 🔹 **Actor Insights**  
✔ The **most frequent actor pairs** have starred in multiple Netflix shows together.  

### 🔹 **TV Show Analysis**  
✔ Many **popular TV shows** have **3+ seasons**, indicating viewer engagement.  

### 🔹 **Content Growth**  
✔ **Netflix’s content library** has significantly **expanded over the years**.  
