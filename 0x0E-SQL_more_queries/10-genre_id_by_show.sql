-- a script that lists all shows contained in hbtn_0d_tvshows that have
-- at least one genre linked

SELECT sh.title, ge.genre_id
FROM tv_shows AS sh
INNER JOIN tv_show_genres AS ge
ON sh.id = ge.show_id
ORDER BY sh.title, ge.genre_id;
