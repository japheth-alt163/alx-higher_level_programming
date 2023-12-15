-- Selects distinct show titles from the tv_shows table
-- for shows without the comedy genre, ordered by ascending show title.

SELECT DISTINCT `title`
FROM `tv_shows` AS t

-- Left joins the tv_show_genres table on show_id
-- and then left joins the resulting table with the tv_genres table on genre_id.
LEFT JOIN `tv_show_genres` AS s ON s.`show_id` = t.`id`
LEFT JOIN `tv_genres` AS g ON g.`id` = s.`genre_id`

-- Filters out shows associated with the comedy genre
-- by using a subquery with the NOT IN clause.
WHERE t.`title` NOT IN (
    SELECT `title`
    FROM `tv_shows` AS t
    INNER JOIN `tv_show_genres` AS s ON s.`show_id` = t.`id`
    INNER JOIN `tv_genres` AS g ON g.`id` = s.`genre_id`
    WHERE g.`name` = "Comedy"
)

-- Orders the result set by ascending show title.
ORDER BY `title`;
