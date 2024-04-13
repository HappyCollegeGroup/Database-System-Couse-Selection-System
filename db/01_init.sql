-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2024-04-12 15:50:33
-- 伺服器版本： 10.4.32-MariaDB
-- PHP 版本： 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

-- 創建DB
CREATE DATABASE testdb;
USE testdb

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
CREATE USER 'hj'@'localhost' IDENTIFIED BY 'test1234';
GRANT ALL PRIVILEGES ON `testdb` . * TO 'hj'@'localhost';
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
-- https://oxygentw.net/blog/computer/new-mysql-user/
