# 🎬 Netflix SQL Analysis Project  
![Netflix Screenshot](https://github.com/your-username/your-repo-name/blob/main/netflix_image.png)   

## 📌 Project  
This project aims to analyze **Netflix's movie and TV show catalog** using **SQL** to uncover **key business insights**. It includes **data exploration, trend analysis, and content distribution insights** to support **data-driven decision-making**.  

---

## 🎯 Objective  
The goal of this project is to:  
✔ Perform **Exploratory Data Analysis (EDA)** on Netflix content.  
✔ Extract **actionable business insights** using **SQL queries**.  
✔ Showcase **basic, intermediate, and advanced SQL skills** (Joins, Window Functions, CTEs, Subqueries).  
✔ Understand **content distribution trends**, **popular actors**, and **regional content patterns**.  

---

## 📊 Dataset  
The dataset contains **Netflix movie and TV show details**, including:  

| Column Name  | Description  |
|-------------|--------------|
| `show_id`   | Unique identifier for each title  |
| `type`      | Type of content (Movie or TV Show)  |
| `title`     | Name of the show  |
| `director`  | Director(s) of the show  |
| `casts`     | List of actors  |
| `country`   | Country of production  |
| `date_added` | Date the show was added to Netflix  |
| `release_year` | Year of release  |
| `rating`    | Content rating (PG, R, etc.)  |
| `duration`  | Duration of movies (in minutes) or TV show seasons  |
| `listed_in` | Genre(s) of the content  |
| `description` | Short summary of the show  |

---

## 📂 Schema  
The database schema consists of a **single table** named `netflix`:  

![Schema Screenshot](path/to/schema_screenshot.png)  

---

## 🏢 Business Problem and Solutions  

### **Problem 1: Which countries produce the most content on Netflix?**  
📌 **Solution**:  
- Count the number of content pieces per country.  
- Rank the countries based on content production.  

🖼 **Query Screenshot**:  
![Top Countries Query](https://github.com/dr-vishakha-gupta/portfolio/blob/main/Netflix-EDA-SQL/Top5Countries.png)  

🖼 **Results Screenshot**:  
![Top Countries Results](path/to/top_countries_results.png)  

**🔍 Findings**: The top **5 countries** with the most Netflix content are identified.  

---

### **Problem 2: What are the most common actor pairings?**  
📌 **Solution**:  
- Extract individual actors from the `casts` column.  
- Find frequent co-appearances in Netflix titles.  

🖼 **Query Screenshot**:  
![Actor Pairings Query](path/to/actor_pairings_query.png)  

🖼 **Results Screenshot**:  
![Actor Pairings Results](path/to/actor_pairings_results.png)  

**🔍 Findings**: Identifies actor pairs that frequently collaborate in Netflix productions.  

---

### **Problem 3: Which TV shows have more than 3 seasons?**  
📌 **Solution**:  
- Extract the number of seasons from the `duration` column.  
- Convert it to an integer and filter shows with **more than 3 seasons**.  

🖼 **Query Screenshot**:  
![TV Shows Query](path/to/tv_shows_query.png)  

🖼 **Results Screenshot**:  
![TV Shows Results](path/to/tv_shows_results.png)  

**🔍 Findings**: Identifies **long-running TV shows** on Netflix.  

---

### **Problem 4: What are the most popular genres on Netflix?**  
📌 **Solution**:  
- Count the number of titles per genre.  

🖼 **Query Screenshot**:  
![Popular Genres Query](path/to/popular_genres_query.png)  

🖼 **Results Screenshot**:  
![Popular Genres Results](path/to/popular_genres_results.png)  

**🔍 Findings**: Identifies the **most popular genres** on Netflix.  

---

### **Problem 5: How has Netflix's content production evolved over time?**  
📌 **Solution**:  
- Count the number of releases per year.  

🖼 **Query Screenshot**:  
![Content Trend Query](path/to/content_trend_query.png)  

🖼 **Results Screenshot**:  
![Content Trend Results](path/to/content_trend_results.png)  

**🔍 Findings**: Shows the **content release trend over the years**.  

---

## 📈 Findings  

### 🔹 **Content Trends**  
✔ The **USA, India, and UK** have the **highest number of Netflix titles**.  
✔ **Dramas and Comedies** are the **most common genres**.  

### 🔹 **Actor Insights**  
✔ The **most frequent actor pairs** have starred in multiple Netflix shows together.  

### 🔹 **TV Show Analysis**  
✔ Many **popular TV shows** have **3+ seasons**, indicating viewer engagement.  

### 🔹 **Content Growth**  
✔ **Netflix’s content library** has significantly **expanded over the years**.  
