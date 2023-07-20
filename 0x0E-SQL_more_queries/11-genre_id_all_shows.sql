-- a script that lists all shows contained in the database hbtn_0d_tvshows
-- after importing the database dump of hbtn_od_tvshows
-- each record displays tv_shows.title, tv_show_genres.genre_id

SELECT sh.title, ge.genre_id
FROM tv_shows AS sh
LEFT JOIN tv_show_genres AS ge
ON sh.id = ge.show_id
ORDER BY sh.title, ge.genre_id;
