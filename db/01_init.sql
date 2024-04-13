-- 創建DB
CREATE DATABASE testdb;

USE testdb;

--
-- 資料庫： `testdb`
--

-- --------------------------------------------------------

--
-- 資料表結構 `course`
--

CREATE TABLE `course` (
  `course_id` varchar(30) NOT NULL,
  `tid` varchar(30) NOT NULL,
  `dept_name` varchar(30) NOT NULL,
  `cname` varchar(30) NOT NULL,
  `compulsory` tinyint(1) NOT NULL,
  `cgrade` varchar(30) NOT NULL,
  `credit` varchar(30) NOT NULL,
  `capicity` varchar(30) NOT NULL,
  PRIMARY KEY (`course_id`)
);





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
-- 資料表結構 `follows`
--

CREATE TABLE `follows` (
  `sid` varchar(15) NOT NULL,
  `course_id` varchar(30) NOT NULL,
  PRIMARY KEY (`sid`,`course_id`)
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
  `time_id` varchar(30) NOT NULL,
  PRIMARY KEY (`sec_id`)
);



-- --------------------------------------------------------

--
-- 資料表結構 `student`
--

CREATE TABLE `student` (
  `sid` varchar(15) NOT NULL,
  `dept_name` varchar(30) DEFAULT NULL,
  `sname` varchar(30) DEFAULT NULL,
  `sgrade` varchar(30) DEFAULT NULL,
  `password` varchar(30) NOT NULL,
  PRIMARY KEY (`sid`)
);



-- --------------------------------------------------------

--
-- 資料表結構 `takes`
--

CREATE TABLE `takes` (
  `sid` varchar(15) NOT NULL,
  `course_id` varchar(30) NOT NULL,
  PRIMARY KEY (`sid`,`course_id`)
);



-- --------------------------------------------------------

--
-- 資料表結構 `teacher`
--

CREATE TABLE `teacher` (
  `tid` varchar(30) NOT NULL,
  `dept_name` varchar(30) NOT NULL,
  `tname` varchar(30) NOT NULL,
  PRIMARY KEY (`tid`)
);



-- --------------------------------------------------------

--
-- 資料表結構 `time`
--

CREATE TABLE `time` (
  `time_id` varchar(30) NOT NULL,
  PRIMARY KEY (`time_id`)
);


-- 創建使用者，帳號: hj，密碼: test1234
-- https://oxygentw.net/blog/computer/new-mysql-user/
CREATE USER 'hj'@'localhost' IDENTIFIED BY 'test1234';
GRANT ALL PRIVILEGES ON `testdb` . * TO 'hj'@'localhost';
