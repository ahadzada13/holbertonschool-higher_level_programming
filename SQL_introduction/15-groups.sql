-- Lists the number of records with the same score in the table second_table
-- Results display the score and the number of records for this score with the label number
-- Sorted by the number of records in descending order
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
