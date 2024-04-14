-- 預選必修課

USE testdb;

INSERT INTO `takes`
SELECT `sid`, `course_id` FROM `student` 
LEFT JOIN `course` USING (`dept_name`)
WHERE `cgrade` = `sgrade` AND compulsory = 1;
