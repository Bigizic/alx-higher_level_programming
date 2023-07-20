--  a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows

SELECT tv.title, ge.name
FROM tv_shows AS tv
LEFT JOIN tv_show_genres AS svg
ON tv.id = svg.show_id
LEFT JOIN tv_genres AS ge
ON svg.genre_id = ge.id
 ORDER BY tv.title, ge.name;
