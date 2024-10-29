-- Listing all records has name value in  the table second_table ordered bt score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
