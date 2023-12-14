-- Use the hbtn_0d_tvshows_rate database.
USE hbtn_0d_tvshows_rate;

-- Select all genres by their rating sum.
SELECT tv_genres.name, SUM(tv_show_genres.rating) AS rating
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
