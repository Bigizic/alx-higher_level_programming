-- a script that computes the score average of all records in the table

FROM `second_table`
SELECT AVG(`score`) AS `average`;
