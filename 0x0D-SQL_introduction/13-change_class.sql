--  a script that removes all records with a score <= 5 in the table

DELETE FROM second_table
WHERE score <= 5;

SELECT score, name FROM second_table
ORDER BY score DESC;
