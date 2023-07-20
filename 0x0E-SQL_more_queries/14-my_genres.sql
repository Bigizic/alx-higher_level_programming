-- a script that uses the hbtn_0d_tvshows database to lists all genres of
-- the show Dexter

SELECT gh.name
FROM tv_genres AS gh
INNER JOIN tv_show_genres AS sv
ON gh.id = sv.genre_id
INNER JOIN tv_shows AS tv
ON tv.id = sv.show_id
WHERE tv.title = "Dexter"
ORDER BY gh.name;
