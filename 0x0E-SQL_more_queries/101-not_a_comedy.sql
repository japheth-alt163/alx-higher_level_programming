-- Use the hbtn_0d_tvshows database.
USE hbtn_0d_tvshows;

-- Select all shows without the genre Comedy.
SELECT DISTINCT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT tv_show_genres.tv_show_id
    FROM tv_show_genres
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title;
