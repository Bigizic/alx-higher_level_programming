-- a script that lists all genres in the database hbtn_0d_tvshows_rate
-- by their rating

SELECT name, sum(rate) AS rating
FROM tv_genres AS tv_g
INNER JOIN tv_show_genres AS sg ON sg.genre_id = tv_g.id
INNER JOIN tv_show_ratings AS tvsr ON tvsr.show_id = sg.show_id
GROUP BY name
ORDER BY rating DESC;
