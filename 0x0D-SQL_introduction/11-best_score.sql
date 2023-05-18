-- Lists all records in the tablewith a score >= 10 i
-- Records are in descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
