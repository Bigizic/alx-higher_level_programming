-- a script that lists all shows from hbtn_0d_tvshows_rate by
-- their rating. Records are ordered by descending order

SELECT title, sum(rate) AS rating
FROM tv_shows AS tv
INNER JOIN tv_show_ratings AS s ON tv.id = s.show_id
GROUP BY title
ORDER BY rating DESC;
