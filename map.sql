-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 26, 2020 at 07:19 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `MAP`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `name` varchar(6) CHARACTER SET utf8 DEFAULT NULL,
  `username` varchar(6) CHARACTER SET utf8 DEFAULT NULL,
  `password` varchar(9) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`name`, `username`, `password`) VALUES
('Admin', 'admin', 'password'),
('Admin2', 'admin2', 'password2');

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `id` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `roll_number` varchar(8) CHARACTER SET utf8 DEFAULT NULL,
  `status` varchar(1) CHARACTER SET utf8 DEFAULT NULL,
  `prof_username` varchar(28) CHARACTER SET utf8 DEFAULT NULL,
  `lecture` varchar(4) CHARACTER SET utf8 DEFAULT NULL,
  `lecture_type` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`id`, `date`, `roll_number`, `status`, `prof_username`, `lecture`, `lecture_type`) VALUES
(65, '2020-01-27 00:00:00', '18bce039', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'ML', 0),
(66, '2020-01-27 00:00:00', '17bit075', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'WD', 1),
(67, '2020-01-27 00:00:00', '17bit085', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'WD', 1),
(72, '2020-01-28 00:00:00', '17bit075', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'DBMS', 2),
(73, '2020-01-28 00:00:00', '17bit075', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'OS', 1),
(74, '2020-01-28 00:00:00', '17bit075', 'A', 'dvijesh.bhatt@nirmauni.ac.in', 'DBMS', 2),
(75, '2020-01-28 00:00:00', '17bit075', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'DBMS', 2),
(76, '2020-01-28 00:00:00', '17bit075', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'DBMS', 2),
(77, '2020-01-30 00:00:00', '17bit075', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'WD', 1),
(78, '2020-01-30 00:00:00', '17bit085', 'A', 'dvijesh.bhatt@nirmauni.ac.in', 'WD', 1),
(79, '2020-01-31 00:00:00', '17bit075', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'DL', 0),
(80, '2020-01-31 00:00:00', '17bit085', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'DL', 0),
(81, '2020-01-31 00:00:00', '17bit075', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'DL', 0),
(82, '2020-01-31 00:00:00', '17bit085', 'A', 'dvijesh.bhatt@nirmauni.ac.in', 'DL', 0),
(83, '2020-01-31 00:00:00', '17bit075', 'A', 'dvijesh.bhatt@nirmauni.ac.in', 'DL', 0),
(84, '2020-01-31 00:00:00', '17bit085', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'DL', 0),
(85, '2020-01-31 00:00:00', '17bit075', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'DL', 0),
(86, '2020-01-31 00:00:00', '17bit085', 'A', 'dvijesh.bhatt@nirmauni.ac.in', 'DL', 0),
(87, '2020-01-31 00:00:00', '17bit075', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'WD', 2),
(88, '2020-01-31 00:00:00', '17bit085', 'A', 'dvijesh.bhatt@nirmauni.ac.in', 'WD', 2),
(89, '2020-01-31 00:00:00', '17bit075', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'WD', 2),
(90, '2020-01-31 00:00:00', '17bit085', 'A', 'dvijesh.bhatt@nirmauni.ac.in', 'WD', 2),
(91, '2020-02-07 00:00:00', '17bit075', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'WD', 1),
(92, '2020-02-07 00:00:00', '17bit085', 'A', 'dvijesh.bhatt@nirmauni.ac.in', 'WD', 1),
(93, '2020-02-26 00:00:00', '17bit075', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'WD', 1),
(94, '2020-02-26 00:00:00', '17bit085', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'WD', 1),
(107, '2020-02-27 00:00:00', '17bit075', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'WD', 1),
(108, '2020-02-27 00:00:00', '17bit085', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'WD', 1),
(113, '2020-03-05 00:00:00', '17bit075', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'WD', 1),
(114, '2020-03-05 00:00:00', '17bit085', 'P', 'dvijesh.bhatt@nirmauni.ac.in', 'WD', 1),
(119, '2020-03-12 00:00:00', '17bit075', 'P', 'Dvijesh Bhatt', 'WD', 1),
(120, '2020-03-12 00:00:00', '17bit085', 'P', 'Dvijesh Bhatt', 'WD', 1),
(121, '2020-03-12 00:00:00', '17bit075', 'P', 'Dvijesh Bhatt', 'WD', 1),
(122, '2020-03-12 00:00:00', '17bit085', 'A', 'Dvijesh Bhatt', 'WD', 1),
(123, '2020-03-13 00:00:00', '17bit075', 'P', 'Dvijesh Bhatt', 'WD', 1),
(124, '2020-03-13 00:00:00', '17bit085', 'A', 'Dvijesh Bhatt', 'WD', 1),
(125, '2020-03-13 00:00:00', '17BCE039', 'A', 'Dvijesh Bhatt', 'ML', 0),
(126, '2020-03-15 00:00:00', '17bit075', 'P', 'Dvijesh Bhatt', 'WD', 1),
(127, '2020-03-15 00:00:00', '17bit085', 'A', 'Dvijesh Bhatt', 'WD', 1),
(128, '2020-05-05 00:00:00', '17bit075', 'P', 'Dvijesh Bhatt', 'WD', 1),
(129, '2020-05-05 00:00:00', '17bit085', 'A', 'Dvijesh Bhatt', 'WD', 1),
(130, '2020-05-19 00:00:00', '17bit075', 'P', 'Dvijesh Bhatt', 'WD', 1),
(131, '2020-05-19 00:00:00', '17bit085', 'A', 'Dvijesh Bhatt', 'WD', 1),
(132, '2020-06-15 00:00:00', '17bit075', 'P', 'Dvijesh Bhatt', 'WD', 1),
(133, '2020-06-15 00:00:00', '17bit085', 'A', 'Dvijesh Bhatt', 'WD', 1),
(134, '2020-09-01 00:00:00', '17bit075', 'A', 'Dvijesh Bhatt', 'WD', 1),
(135, '2020-09-01 00:00:00', '17bit085', 'A', 'Dvijesh Bhatt', 'WD', 1);

-- --------------------------------------------------------

--
-- Table structure for table `facultyadvisor`
--

CREATE TABLE `facultyadvisor` (
  `name` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `username` varchar(31) CHARACTER SET utf8 DEFAULT NULL,
  `password` varchar(31) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `facultyadvisor`
--

INSERT INTO `facultyadvisor` (`name`, `username`, `password`) VALUES
('Dvijesh Bhatt', 'dvijesh.bhatt@nirmauni.ac.in', 'dvijesh.bhatt@nirmauni.ac.in'),
('Jaiprakash Verma', 'jaiprakash.verma@nirmauni.ac.in', 'jaiprakash.verma@nirmauni.ac.in');

-- --------------------------------------------------------

--
-- Table structure for table `professor`
--

CREATE TABLE `professor` (
  `name` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  `username` varchar(31) CHARACTER SET utf8 DEFAULT NULL,
  `password` varchar(31) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `professor`
--

INSERT INTO `professor` (`name`, `username`, `password`) VALUES
('Dvijesh Bhatt', 'dvijesh.bhatt@nirmauni.ac.in', 'dvijesh.bhatt@nirmauni.ac.in'),
('Jaiprakash Verma', 'jaiprakash.verma@nirmauni.ac.in', 'jaiprakash.verma@nirmauni.ac.in');

-- --------------------------------------------------------

--
-- Table structure for table `professortimetable`
--

CREATE TABLE `professortimetable` (
  `id` int(11) DEFAULT NULL,
  `prof_username` varchar(28) CHARACTER SET utf8 DEFAULT NULL,
  `day` varchar(7) CHARACTER SET utf8 DEFAULT NULL,
  `class_name` varchar(6) CHARACTER SET utf8 DEFAULT NULL,
  `lecture` varchar(2) CHARACTER SET utf8 DEFAULT NULL,
  `end_time` varchar(8) CHARACTER SET utf8 DEFAULT NULL,
  `start_time` varchar(8) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `professortimetable`
--

INSERT INTO `professortimetable` (`id`, `prof_username`, `day`, `class_name`, `lecture`, `end_time`, `start_time`) VALUES
(1, 'dvijesh.bhatt@nirmauni.ac.in', 'monday', '6ITB1', 'WD', '09:50:00', '09:00:00'),
(2, 'dvijesh.bhatt@nirmauni.ac.in', 'monday', '6ITBT1', 'WD', '10:50:00', '09:50:00'),
(3, 'dvijesh.bhatt@nirmauni.ac.in', 'monday', '-', '-', '18:05:00', '11:15:00'),
(4, 'dvijesh.bhatt@nirmauni.ac.in', 'tuesday', '-', '-', '09:50:00', '09:00:00'),
(5, 'dvijesh.bhatt@nirmauni.ac.in', 'tuesday', '6CEA', 'ML', '10:50:00', '09:50:00'),
(6, 'dvijesh.bhatt@nirmauni.ac.in', 'tuesday', '6ITB', 'DL', '13:15:00', '11:15:00'),
(7, 'dvijesh.bhatt@nirmauni.ac.in', 'tuesday', '-', '-', '18:05:00', '14:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `roll_number` varchar(8) CHARACTER SET utf8 DEFAULT NULL,
  `name` varchar(18) CHARACTER SET utf8 DEFAULT NULL,
  `branch` varchar(2) CHARACTER SET utf8 DEFAULT NULL,
  `semester` int(11) DEFAULT NULL,
  `username` varchar(23) CHARACTER SET utf8 DEFAULT NULL,
  `password` varchar(23) CHARACTER SET utf8 DEFAULT NULL,
  `lab_batch` varchar(2) CHARACTER SET utf8 DEFAULT NULL,
  `tut_batch` varchar(2) CHARACTER SET utf8 DEFAULT NULL,
  `batch` varchar(1) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`roll_number`, `name`, `branch`, `semester`, `username`, `password`, `lab_batch`, `tut_batch`, `batch`) VALUES
('17bit075', 'Parth Patel', 'IT', 7, '17bit075@nirmauni.ac.in', '17bit075@nirmauni.ac.in', 'B1', 'T1', 'B'),
('17bit061', 'Nisarg Bhatt', 'IT', 7, '17bit061@nirmauni.ac.in', '17bit061@nirmauni.ac.in', 'A4', 'T4', 'A'),
('17bit085', 'Himanshu Prajapati', 'IT', 7, '17bit085@nirmauni.ac.in', '17bit085@nirmauni.ac.in', 'B1', 'T1', 'B'),
('17bit046', 'Siddharth Marvania', 'IT', 7, '17bit046@nirmauni.ac.in', '17bit046@nirmauni.ac.in', 'A3', 'T3', 'A'),
('17bit034', 'Kandarp Kakkad', 'IT', 7, '17bit034@nirmauni.ac.in', '17bit034@nirmauni.ac.in', 'A2', 'T2', 'A');

-- --------------------------------------------------------

--
-- Table structure for table `studentsubject`
--

CREATE TABLE `studentsubject` (
  `id` int(11) DEFAULT NULL,
  `branch` varchar(2) CHARACTER SET utf8 DEFAULT NULL,
  `semester` int(11) DEFAULT NULL,
  `lecture` varchar(4) CHARACTER SET utf8 DEFAULT NULL,
  `lecture_type` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studentsubject`
--

INSERT INTO `studentsubject` (`id`, `branch`, `semester`, `lecture`, `lecture_type`) VALUES
(1, 'IT', 7, 'WD', 1),
(2, 'IT', 7, 'WD', 0),
(3, 'IT', 7, 'WD', 2),
(4, 'IT', 7, 'DBMS', 0),
(5, 'IT', 7, 'DBMS', 1),
(6, 'IT', 7, 'OS', 1),
(7, 'IT', 7, 'DBMS', 2),
(8, 'IT', 7, 'DL', 0),
(9, 'IT', 7, 'DL', 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
