-- phpMyAdmin SQL Dump
-- version 3.5.5
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2015 年 04 月 18 日 20:23
-- 服务器版本: 5.5.29
-- PHP 版本: 5.4.10

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `animal_shelter`
--

-- --------------------------------------------------------

--
-- 表的结构 `animal`
--

CREATE TABLE `animals` (
  `id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `animal_subid` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `animal_area_pkid` int(11) NOT NULL,
  `animal_shelter_pkid` int(11) NOT NULL,
  `animal_place` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `animal_kind` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `animal_sex` varchar(2) COLLATE utf8_unicode_ci NOT NULL,
  `animal_bodytype` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `animal_colour` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `animal_age` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `animal_sterilization` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `animal_bacterin` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `animal_foundplace` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `animal_title` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `animal_status` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `animal_remark` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `animal_caption` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `animal_opendate` datetime NOT NULL,
  `animal_closeddate` datetime NOT NULL,
  `animal_update` datetime NOT NULL,
  `animal_createtime` datetime NOT NULL,
  `shelter_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `album_update` datetime NOT NULL,
  PRIMARY KEY (`animal_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
