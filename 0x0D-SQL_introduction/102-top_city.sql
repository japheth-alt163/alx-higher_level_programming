-- Display top 3 cities' temperatures during July and August ordered by temperature (descending)
SELECT city, ROUND(AVG(temperature), 4) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)  -- Filter for July and August
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
