--  a script that removes all records with a score <= 5 in the table

ALTER TABLE `second_table`
DROP COLUMN `score`
WHERE `score` <= 5;

