-- listing all cities and their states
SELECT c.id id, c.name name, s.name name FROM cities c INNER JOIN states s ON c.state_id = s.id ORDER BY c.id;
