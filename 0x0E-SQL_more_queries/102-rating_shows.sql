-- a script that lists all shows from hbtn_0d_tvshows_rate by
-- their rating. Records are ordered by descending order

SELECT title, sum(rate) AS r
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY r DESC;
