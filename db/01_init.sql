-- 創建DB
CREATE DATABASE testdb;

USE testdb;

--
-- 資料庫： `testdb`
--

-- --------------------------------------------------------

--
-- 資料表結構 `department`
--

CREATE TABLE `department` (
  `dept_name` varchar(30) NOT NULL,
  PRIMARY KEY (`dept_name`)
);

-- --------------------------------------------------------

--
-- 資料表結構 `student`
--

CREATE TABLE `student` (
  `sid` varchar(15) NOT NULL,
  `dept_name` varchar(30) NOT NULL,
  `sname` varchar(30) NOT NULL,
  `sgrade` int NOT NULL,
  `password` varchar(30) NOT NULL,
  PRIMARY KEY (`sid`),
  FOREIGN KEY (`dept_name`) REFERENCES `department` (`dept_name`)
);

-- --------------------------------------------------------

--
-- 資料表結構 `teacher`
--

CREATE TABLE `teacher` (
  `tid` varchar(30) NOT NULL,
  `dept_name` varchar(30) NOT NULL,
  `tname` varchar(30) NOT NULL,
  PRIMARY KEY (`tid`),
  FOREIGN KEY (`dept_name`) REFERENCES `department` (`dept_name`)
);

-- --------------------------------------------------------

--
-- 資料表結構 `course`
--

CREATE TABLE `course` (
  `course_id` varchar(30) NOT NULL,
  `tid` varchar(30) NOT NULL,
  `dept_name` varchar(30) NOT NULL,
  `cname` varchar(30) NOT NULL,
  `compulsory` BOOLEAN NOT NULL,
  `cgrade` int NOT NULL,
  `credit` int NOT NULL,
  `capicity` int NOT NULL,
  PRIMARY KEY (`course_id`),
  FOREIGN KEY (`tid`) REFERENCES `teacher` (`tid`),
  FOREIGN KEY (`dept_name`) REFERENCES `department` (`dept_name`)
);

-- --------------------------------------------------------

--
-- 資料表結構 `takes`
--

CREATE TABLE `takes` (
  `sid` varchar(15) NOT NULL,
  `course_id` varchar(30) NOT NULL,
  PRIMARY KEY (`sid`,`course_id`),
  FOREIGN KEY (`sid`) REFERENCES `student` (`sid`),
  FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`)
);

-- --------------------------------------------------------

--
-- 資料表結構 `follows`
--

CREATE TABLE `follows` (
  `sid` varchar(15) NOT NULL,
  `course_id` varchar(30) NOT NULL,
  PRIMARY KEY (`sid`,`course_id`),
  FOREIGN KEY (`sid`) REFERENCES `student` (`sid`),
  FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`)
);

-- --------------------------------------------------------

--
-- 資料表結構 `time`
--

CREATE TABLE `time` (
  `time_id` int NOT NULL,
  PRIMARY KEY (`time_id`)
);

-- --------------------------------------------------------

--
-- 資料表結構 `location`
--

CREATE TABLE `location` (
  `loc_name` varchar(30) NOT NULL,
  PRIMARY KEY (`loc_name`)
);

-- --------------------------------------------------------

--
-- 資料表結構 `section`
--

CREATE TABLE `section` (
  `sec_id` varchar(30) NOT NULL,
  `course_id` varchar(30) NOT NULL,
  `loc_name` varchar(30) NOT NULL,
  `time_id` int NOT NULL,
  PRIMARY KEY (`sec_id`),
  FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`),
  FOREIGN KEY (`loc_name`) REFERENCES `location` (`loc_name`),
  FOREIGN KEY (`time_id`) REFERENCES `time` (`time_id`)
);


-- 創建使用者，帳號: hj，密碼: test1234
-- https://oxygentw.net/blog/computer/new-mysql-user/
CREATE USER 'hj'@'localhost' IDENTIFIED BY 'test1234';
GRANT ALL PRIVILEGES ON `testdb` . * TO 'hj'@'localhost';
