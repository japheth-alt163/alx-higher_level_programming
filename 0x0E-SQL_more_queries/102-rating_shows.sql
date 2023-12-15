-- Selects the title of shows and their total rating from the tv_shows table
-- by joining with the tv_show_ratings table on show_id.
-- The result is grouped by show title and ordered by descending rating.

SELECT `title`, SUM(`rate`) AS `rating`
FROM `tv_shows` AS t

-- Joins the tv_shows table with the tv_show_ratings table on show_id.
INNER JOIN `tv_show_ratings` AS r ON t.`id` = r.`show_id`

-- Groups the result set by show title.
GROUP BY `title`

-- Orders the result set by descending total rating.
ORDER BY `rating` DESC;
