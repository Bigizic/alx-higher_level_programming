-- a script that displays the average temperature

SELECT `city`, AVG(`value`) AS `a_tmp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `a_tmp` DESC;
