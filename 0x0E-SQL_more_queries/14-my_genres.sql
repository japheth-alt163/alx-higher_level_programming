-- Use the hbtn_0d_tvshows database.
USE hbtn_0d_tvshows;

-- Select genres of the show Dexter from tv_show_genres and tv_genres tables.
SELECT tv_genres.name
FROM tv_show_genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;
