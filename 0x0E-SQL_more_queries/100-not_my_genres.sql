-- Selects distinct genre names from the tv_genres table
-- for genres not linked to the show Dexter, sorted by ascending genre name.

SELECT DISTINCT `name`
FROM `tv_genres` AS g

-- Joins the tv_genres table with the tv_show_genres table on genre_id
-- and then joins the resulting table with the tv_shows table on show_id.
INNER JOIN `tv_show_genres` AS s ON g.`id` = s.`genre_id`
INNER JOIN `tv_shows` AS t ON s.`show_id` = t.`id`

-- Filters out genres associated with the show Dexter
-- by using a subquery with the NOT IN clause.
WHERE g.`name` NOT IN (
    SELECT `name`
    FROM `tv_genres` AS g
    INNER JOIN `tv_show_genres` AS s ON g.`id` = s.`genre_id`
    INNER JOIN `tv_shows` AS t ON s.`show_id` = t.`id`
    WHERE t.`title` = "Dexter"
)

-- Orders the result set by ascending genre name.
ORDER BY g.`name`;
