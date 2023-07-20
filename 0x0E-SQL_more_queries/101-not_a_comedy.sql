-- a script that lists all shows without the genre Comedy in the database
-- hbtn_0d_tvshows

SET @comedy_id = (SELECT id FROM tv_genres WHERE name = "Comedy");
SELECT title
FROM tv_shows
WHERE id NOT IN (
	SELECT show_id
	FROM tv_show_genres
	WHERE genre_id = @comedy_id
)
ORDER BY title ASC;
