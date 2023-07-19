-- a script that lists all the cities of California that can be found
-- in the database hbtn_0d_usa

SET @state_id = (SELECT id FROM states WHERE name = 'California');
SELECT id, name
FROM cities
WHERE state_id = @state_id
ORDER BY id;
