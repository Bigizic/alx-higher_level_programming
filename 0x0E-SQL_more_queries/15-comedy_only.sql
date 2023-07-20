-- a script that lists all Comedy shows in the database hbtn_0d_tvshows

SELECT tv.title
FROM tv_shows AS tv
INNER JOIN tv_show_genres AS svg
ON tv.id = svg.show_id
INNER JOIN tv_genres AS ge
ON ge.id = svg.genre_id
WHERE ge.name = "Comedy"
ORDER BY tv.title;
