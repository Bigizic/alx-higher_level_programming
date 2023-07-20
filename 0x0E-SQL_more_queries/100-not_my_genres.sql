--  a script that uses the hbtn_0d_tvshows database to list all genres
-- not linked to the show Dexter

SET @dexter_genre_id = (SELECT id FROM tv_shows WHERE title = 'Dexter');
SELECT name
FROM tv_genres
WHERE id NOT IN (
	SELECT genre_id
	FROM tv_show_genres
	WHERE show_id = @dexter_genre_id
)
ORDER BY name ASC;
