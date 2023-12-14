-- Use the hbtn_0d_usa database.
USE hbtn_0d_usa;

-- Select cities and corresponding state names using a JOIN.
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
