-- Write a script that displays the max temperature of each state (ordered by State name).
-- from the imported database: Temperatures #0

SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state LIMIT 3;
