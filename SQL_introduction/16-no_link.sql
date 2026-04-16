-- Lists all records of the table second_table (database hbtn_0c_0)
-- Doesn't list rows without a name value
-- Results display score and name, ordered by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name <> "" ORDER BY score DESC;
