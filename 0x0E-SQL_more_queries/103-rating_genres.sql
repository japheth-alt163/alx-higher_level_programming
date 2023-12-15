-- Selects the name of genres and their total rating from the tv_genres table
-- by joining with the tv_show_genres table on genre_id and then joining
-- with the tv_show_ratings table on show_id.
-- The result is grouped by genre name and ordered by descending rating.

SELECT `name`, SUM(`rate`) AS `rating`
FROM `tv_genres` AS g

-- Joins the tv_genres table with the tv_show_genres table on genre_id.
INNER JOIN `tv_show_genres` AS s ON s.`genre_id` = g.`id`

-- Joins the resulting table with the tv_show_ratings table on show_id.
INNER JOIN `tv_show_ratings` AS r ON r.`show_id` = s.`show_id`

-- Groups the result set by genre name.
GROUP BY `name`

-- Orders the result set by descending total rating.
ORDER BY `rating` DESC;
