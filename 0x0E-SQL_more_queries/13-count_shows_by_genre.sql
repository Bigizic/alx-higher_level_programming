-- a script that lists all genres from hbtn_0d_tvshows and displays the
-- number of shows linked to each

SELECT ge.name AS genre,
COUNT(*) AS number_of_shows
FROM tv_genres AS ge
INNER JOIN tv_show_genres AS tv
ON ge.id = tv.genre_id
GROUP BY ge.name
ORDER BY number_of_shows DESC;
