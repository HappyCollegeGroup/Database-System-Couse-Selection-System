-- 創建DB
CREATE DATABASE testdb;
-- 創建TABLE
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
  `compulsory` varchar(30) NOT NULL,
  `cgrade` varchar(30) NOT NULL,
  `credit` varchar(30) NOT NULL,
  `capicity` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `department`
--

CREATE TABLE `department` (
  `dept_name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `follows`
--

CREATE TABLE `follows` (
  `sid` varchar(15) NOT NULL,
  `course_id` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `follows`
--



-- --------------------------------------------------------

--
-- 資料表結構 `location`
--

CREATE TABLE `location` (
  `loc_name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `section`
--

CREATE TABLE `section` (
  `sec_id` varchar(30) NOT NULL,
  `course_id` varchar(30) NOT NULL,
  `loc_name` varchar(30) NOT NULL,
  `time_id` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `student`
--

CREATE TABLE `student` (
  `sid` varchar(15) NOT NULL,
  `dept_name` varchar(30) DEFAULT NULL,
  `sname` varchar(30) DEFAULT NULL,
  `sgrade` varchar(30) DEFAULT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `student`
--

-- --------------------------------------------------------

--
-- 資料表結構 `takes`
--

CREATE TABLE `takes` (
  `sid` varchar(15) NOT NULL,
  `course_id` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `teacher`
--

CREATE TABLE `teacher` (
  `tid` varchar(30) NOT NULL,
  `dept_name` int(30) NOT NULL,
  `tname` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `time`
--

CREATE TABLE `time` (
  `time_id` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`course_id`);

--
-- 資料表索引 `follows`
--
ALTER TABLE `follows`
  ADD PRIMARY KEY (`sid`,`course_id`);

--
-- 資料表索引 `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`loc_name`);

--
-- 資料表索引 `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`sid`);

--
-- 資料表索引 `takes`
--
ALTER TABLE `takes`
  ADD PRIMARY KEY (`sid`,`course_id`);

--
-- 資料表索引 `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`tid`);

--
-- 資料表索引 `time`
--
ALTER TABLE `time`
  ADD PRIMARY KEY (`time_id`);
COMMIT;
-- 創建使用者，帳號: hj，密碼: test1234
CREATE USER 'hj'@'localhost' IDENTIFIED BY 'test1234';
GRANT ALL PRIVILEGES ON `testdb` . * TO 'hj'@'localhost';
-- https://oxygentw.net/blog/computer/new-mysql-user/
