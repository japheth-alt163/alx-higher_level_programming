-- Use the hbtn_0d_tvshows database.
USE hbtn_0d_tvshows;

-- Select shows and corresponding genre IDs from tv_shows and tv_show_genres tables.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
