-- a script that lists all shows from hbtn_0d_tvshows_rate by theirg
-- rating, Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating

SELECT CONCAT(tv_shows.title, ' - ', SUM(tv_show_ratings.rate)) AS `tv_show - rating sum`
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY SUM(tv_show_ratings.rate) DESC;
