-- 1. Count the total number of records in the dataset
SELECT COUNT(*) AS total_records FROM netflix;

-- 2. Check for missing values in key columns (title, director, country)
SELECT 
    SUM(CASE WHEN title IS NULL THEN 1 ELSE 0 END) AS missing_title,
    SUM(CASE WHEN director IS NULL THEN 1 ELSE 0 END) AS missing_director,
    SUM(CASE WHEN country IS NULL THEN 1 ELSE 0 END) AS missing_country
FROM netflix;

-- 3. Count distinct values in important columns (type, country, rating)
SELECT COUNT(DISTINCT type) AS unique_types FROM netflix;
SELECT COUNT(DISTINCT country) AS unique_countries FROM netflix;
SELECT COUNT(DISTINCT rating) AS unique_ratings FROM netflix;

-- 4. Check for duplicate records based on title
SELECT title, COUNT(*) AS duplicate_count
FROM netflix 
GROUP BY title 
HAVING COUNT(*) > 1;

-- 4.1 Get a count of total records in the dataset
SELECT COUNT(*) AS total_records FROM netflix;

-- 4.2 List all unique types of content (Movies vs. TV Shows)
SELECT DISTINCT type FROM netflix;

-- 4.3 Count of Movies vs. TV Shows
SELECT type, COUNT(*) AS total_count 
FROM netflix 
GROUP BY type;

-- 4.4 Find the most common content rating
SELECT rating, COUNT(*) AS total_count 
FROM netflix 
GROUP BY rating 
ORDER BY total_count DESC;

-- 4.5 Find the oldest and newest release years
SELECT MIN(release_year) AS oldest_year, MAX(release_year) AS latest_year FROM netflix;

-- 5.1 Count of content by country (Top 10)
SELECT country, COUNT(*) AS total_count
FROM netflix
WHERE country IS NOT NULL
GROUP BY country
ORDER BY total_count DESC
LIMIT 10;

-- 5.2 Find the most frequently occurring director
SELECT director, COUNT(*) AS num_movies
FROM netflix
WHERE director IS NOT NULL
GROUP BY director
ORDER BY num_movies DESC
LIMIT 1;

-- 5.3 Count of movies by genre
SELECT listed_in AS genre, COUNT(*) AS total_count
FROM netflix
GROUP BY listed_in
ORDER BY total_count DESC;

-- 5.4 Find all TV Shows with more than 3 seasons
SELECT title, duration
FROM netflix
WHERE type = 'TV Show' 
AND duration REGEXP '^[0-9]+ season'
AND CAST(SUBSTRING_INDEX(duration, ' ', 1) AS UNSIGNED) > 3;

-- 5.5 Identify directors with content in multiple genres
SELECT director, COUNT(DISTINCT listed_in) AS unique_genres
FROM netflix
WHERE director IS NOT NULL
GROUP BY director
ORDER BY unique_genres DESC
LIMIT 5;

-- 6.1 Rank top 5 countries by average yearly content release
SELECT country, avg_releases_per_year
FROM (
    SELECT country, ROUND(AVG(content_count), 2) AS avg_releases_per_year
    FROM (
        SELECT country, release_year, COUNT(*) AS content_count
        FROM netflix
        WHERE country IS NOT NULL
        GROUP BY country, release_year
    ) AS yearly_content
    GROUP BY country
    ORDER BY avg_releases_per_year DESC
    LIMIT 5
) AS ranked_countries;

-- 6.2 Identify most frequent actor pairings
WITH actor_exploded AS (
    SELECT show_id, 
           SUBSTRING_INDEX(SUBSTRING_INDEX(`casts`, ', ', n.digit), ', ', -1) AS actor
    FROM netflix
    JOIN (SELECT 1 AS digit UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5) AS n
    ON CHAR_LENGTH(`casts`) - CHAR_LENGTH(REPLACE(`casts`, ', ', '')) >= n.digit - 1
    WHERE `casts` IS NOT NULL
)
SELECT a1.actor AS actor_1, a2.actor AS actor_2, COUNT(*) AS total_appearances
FROM actor_exploded a1
JOIN actor_exploded a2 
ON a1.show_id = a2.show_id AND a1.actor < a2.actor
GROUP BY actor_1, actor_2
ORDER BY total_appearances DESC
LIMIT 3;

-- 6.3 Find the longest gap between a director's releases
WITH director_movies AS (
    SELECT director, release_year, 
           LAG(release_year) OVER (PARTITION BY director ORDER BY release_year) AS prev_release
    FROM netflix
    WHERE director IS NOT NULL
)
SELECT director, MAX(release_year - prev_release) AS max_gap
FROM director_movies
WHERE prev_release IS NOT NULL
GROUP BY director
ORDER BY max_gap DESC
LIMIT 1;

-- 6.4 Analyze the growth rate of Netflix content over the years
WITH yearly_counts AS (
    SELECT release_year, COUNT(*) AS total_content
    FROM netflix
    WHERE release_year IS NOT NULL
    GROUP BY release_year
)
SELECT release_year, total_content, 
       LAG(total_content) OVER (ORDER BY release_year) AS prev_year_count,
       ROUND(((total_content - LAG(total_content) OVER (ORDER BY release_year)) * 100.0 / 
              LAG(total_content) OVER (ORDER BY release_year)), 2) AS growth_rate
FROM yearly_counts
ORDER BY release_year DESC;

-- 6.5 Find the highest-rated content per year
WITH yearly_best AS (
    SELECT release_year, title, rating,
           RANK() OVER (PARTITION BY release_year ORDER BY rating DESC) AS rnk
    FROM netflix
    WHERE rating IS NOT NULL
)
SELECT release_year, title, rating
FROM yearly_best
WHERE rnk = 1;
