-- Script displays the max temperature of each state
-- Query to display the max temperature of each state
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY State
ORDER BY state;

