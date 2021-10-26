-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: Insurance_company
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.20.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Beneficiaries`
--
DROP DATABASE IF EXISTS dna_database;
CREATE SCHEMA dna_database;
USE dna_database;

DROP TABLE IF EXISTS `Beneficiaries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Beneficiaries` (
  `policy_id` varchar(15) NOT NULL,
  `name_of_beneficiary` varchar(100) NOT NULL,
  PRIMARY KEY (`policy_id`,`name_of_beneficiary`),
  FULLTEXT KEY `name_of_beneficiary` (`name_of_beneficiary`),
  CONSTRAINT `Beneficiaries_ibfk_1` FOREIGN KEY (`policy_id`) REFERENCES `Life` (`policy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Beneficiaries`
--

LOCK TABLES `Beneficiaries` WRITE;
/*!40000 ALTER TABLE `Beneficiaries` DISABLE KEYS */;
INSERT INTO `Beneficiaries` VALUES ('Life#234567','Rohit'),('Life#234567','Sumit');
/*!40000 ALTER TABLE `Beneficiaries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cashless_Hospitals`
--

DROP TABLE IF EXISTS `Cashless_Hospitals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cashless_Hospitals` (
  `policy_id` varchar(15) NOT NULL,
  `name_of_hospital` varchar(50) NOT NULL,
  PRIMARY KEY (`policy_id`,`name_of_hospital`),
  FULLTEXT KEY `name_of_hospital` (`name_of_hospital`),
  CONSTRAINT `Cashless_Hospitals_ibfk_1` FOREIGN KEY (`policy_id`) REFERENCES `Medical` (`policy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cashless_Hospitals`
--

LOCK TABLES `Cashless_Hospitals` WRITE;
/*!40000 ALTER TABLE `Cashless_Hospitals` DISABLE KEYS */;
INSERT INTO `Cashless_Hospitals` VALUES ('medi#123456','Galaxy-Care-Hospital'),('medi#123456','Kohinoor-International-Hospital');
/*!40000 ALTER TABLE `Cashless_Hospitals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Claim_Date`
--

DROP TABLE IF EXISTS `Claim_Date`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Claim_Date` (
  `policy_id` varchar(15) NOT NULL,
  `date_of_claim` date NOT NULL,
  PRIMARY KEY (`policy_id`),
  CONSTRAINT `Claim_Date_ibfk_1` FOREIGN KEY (`policy_id`) REFERENCES `Resolves_Claims` (`policy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Claim_Date`
--

LOCK TABLES `Claim_Date` WRITE;
/*!40000 ALTER TABLE `Claim_Date` DISABLE KEYS */;
INSERT INTO `Claim_Date` VALUES ('hous#345678','2010-01-01');
/*!40000 ALTER TABLE `Claim_Date` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Claim_Report`
--

DROP TABLE IF EXISTS `Claim_Report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Claim_Report` (
  `policy_id` varchar(15) NOT NULL,
  `claim_report` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`policy_id`),
  CONSTRAINT `Claim_Report_ibfk_1` FOREIGN KEY (`policy_id`) REFERENCES `Resolves_Claims` (`policy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Claim_Report`
--

LOCK TABLES `Claim_Report` WRITE;
/*!40000 ALTER TABLE `Claim_Report` DISABLE KEYS */;
INSERT INTO `Claim_Report` VALUES ('hous#345678','House burned down due to gas leak.-Categorized as accident.-Claim Approved.');
/*!40000 ALTER TABLE `Claim_Report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Conditions_Covered`
--

DROP TABLE IF EXISTS `Conditions_Covered`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Conditions_Covered` (
  `policy_id` varchar(15) NOT NULL,
  `name_of_condition` varchar(50) NOT NULL,
  PRIMARY KEY (`policy_id`,`name_of_condition`),
  FULLTEXT KEY `name_of_condition` (`name_of_condition`),
  CONSTRAINT `Conditions_Covered_ibfk_1` FOREIGN KEY (`policy_id`) REFERENCES `Medical` (`policy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Conditions_Covered`
--

LOCK TABLES `Conditions_Covered` WRITE;
/*!40000 ALTER TABLE `Conditions_Covered` DISABLE KEYS */;
INSERT INTO `Conditions_Covered` VALUES ('medi#123456','Covid-19'),('medi#123456','Dengue'),('medi#123456','Injury'),('medi#123456','Malaria');
/*!40000 ALTER TABLE `Conditions_Covered` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `aadhar_no` varchar(20) NOT NULL,
  `date_of_birth` date NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) DEFAULT NULL,
  `surname` varchar(50) DEFAULT NULL,
  `email_id` varchar(100) NOT NULL,
  `customer_status` varchar(15) DEFAULT 'normal',
  `street_address` varchar(100) NOT NULL,
  `zip_code` varchar(6) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  PRIMARY KEY (`aadhar_no`),
  FULLTEXT KEY `first_name` (`first_name`,`middle_name`,`surname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES ('567812340987','2000-11-05','Alok','Kumar','Arora','alok@gmail.com','Gold','Jepis Nagar','654321','Noida','UP');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer_Age`
--

DROP TABLE IF EXISTS `Customer_Age`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer_Age` (
  `age` int NOT NULL,
  `customer_aadhar_no` varchar(20) NOT NULL,
  PRIMARY KEY (`age`,`customer_aadhar_no`),
  KEY `customer_aadhar_no` (`customer_aadhar_no`),
  CONSTRAINT `Customer_Age_ibfk_1` FOREIGN KEY (`customer_aadhar_no`) REFERENCES `Customer` (`aadhar_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer_Age`
--

LOCK TABLES `Customer_Age` WRITE;
/*!40000 ALTER TABLE `Customer_Age` DISABLE KEYS */;
INSERT INTO `Customer_Age` VALUES (19,'567812340987');
/*!40000 ALTER TABLE `Customer_Age` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer_Contact`
--

DROP TABLE IF EXISTS `Customer_Contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer_Contact` (
  `contact_number` varchar(15) NOT NULL,
  `customer_aadhar_no` varchar(20) NOT NULL,
  PRIMARY KEY (`contact_number`,`customer_aadhar_no`),
  KEY `customer_aadhar_no` (`customer_aadhar_no`),
  CONSTRAINT `Customer_Contact_ibfk_1` FOREIGN KEY (`customer_aadhar_no`) REFERENCES `Customer` (`aadhar_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer_Contact`
--

LOCK TABLES `Customer_Contact` WRITE;
/*!40000 ALTER TABLE `Customer_Contact` DISABLE KEYS */;
INSERT INTO `Customer_Contact` VALUES ('6388181026','567812340987'),('9415617669','567812340987');
/*!40000 ALTER TABLE `Customer_Contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer_Dependant`
--

DROP TABLE IF EXISTS `Customer_Dependant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer_Dependant` (
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `date_of_birth` date NOT NULL,
  PRIMARY KEY (`first_name`,`middle_name`,`surname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer_Dependant`
--

LOCK TABLES `Customer_Dependant` WRITE;
/*!40000 ALTER TABLE `Customer_Dependant` DISABLE KEYS */;
INSERT INTO `Customer_Dependant` VALUES ('Nitin','Kumar','Arora','2001-12-06');
/*!40000 ALTER TABLE `Customer_Dependant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer_Dependant_Age`
--

DROP TABLE IF EXISTS `Customer_Dependant_Age`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer_Dependant_Age` (
  `dependant_first_name` varchar(50) NOT NULL,
  `dependant_middle_name` varchar(50) NOT NULL,
  `dependant_surname` varchar(50) NOT NULL,
  `age` int NOT NULL,
  PRIMARY KEY (`dependant_first_name`,`dependant_middle_name`,`dependant_surname`,`age`),
  CONSTRAINT `Customer_Dependant_Age_ibfk_1` FOREIGN KEY (`dependant_first_name`, `dependant_middle_name`, `dependant_surname`) REFERENCES `Customer_Dependant` (`first_name`, `middle_name`, `surname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer_Dependant_Age`
--

LOCK TABLES `Customer_Dependant_Age` WRITE;
/*!40000 ALTER TABLE `Customer_Dependant_Age` DISABLE KEYS */;
INSERT INTO `Customer_Dependant_Age` VALUES ('Nitin','Kumar','Arora',18);
/*!40000 ALTER TABLE `Customer_Dependant_Age` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer_License_No`
--

DROP TABLE IF EXISTS `Customer_License_No`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer_License_No` (
  `policy_id` varchar(15) NOT NULL,
  `customer_license_no` varchar(18) NOT NULL,
  PRIMARY KEY (`policy_id`,`customer_license_no`),
  CONSTRAINT `Customer_License_No_ibfk_1` FOREIGN KEY (`policy_id`) REFERENCES `Vehicle` (`policy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer_License_No`
--

LOCK TABLES `Customer_License_No` WRITE;
/*!40000 ALTER TABLE `Customer_License_No` DISABLE KEYS */;
INSERT INTO `Customer_License_No` VALUES ('vehi#570852','379467087330');
/*!40000 ALTER TABLE `Customer_License_No` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Depends_On`
--

DROP TABLE IF EXISTS `Depends_On`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Depends_On` (
  `dependant_first_name` varchar(50) NOT NULL,
  `dependant_middle_name` varchar(50) NOT NULL,
  `dependant_surname` varchar(50) NOT NULL,
  `customer_aadhar_no` varchar(20) NOT NULL,
  PRIMARY KEY (`dependant_first_name`,`dependant_middle_name`,`dependant_surname`,`customer_aadhar_no`),
  KEY `customer_aadhar_no` (`customer_aadhar_no`),
  CONSTRAINT `Depends_On_ibfk_1` FOREIGN KEY (`dependant_first_name`, `dependant_middle_name`, `dependant_surname`) REFERENCES `Customer_Dependant` (`first_name`, `middle_name`, `surname`),
  CONSTRAINT `Depends_On_ibfk_2` FOREIGN KEY (`customer_aadhar_no`) REFERENCES `Customer` (`aadhar_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Depends_On`
--

LOCK TABLES `Depends_On` WRITE;
/*!40000 ALTER TABLE `Depends_On` DISABLE KEYS */;
INSERT INTO `Depends_On` VALUES ('Nitin','Kumar','Arora','567812340987');
/*!40000 ALTER TABLE `Depends_On` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee`
--

DROP TABLE IF EXISTS `Employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee` (
  `department_no` int NOT NULL,
  `serial_no` int NOT NULL,
  `aadhar_no` varchar(20) NOT NULL,
  `date_of_birth` date NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) DEFAULT NULL,
  `surname` varchar(50) DEFAULT NULL,
  `email_id` varchar(100) NOT NULL,
  `street_address` varchar(100) NOT NULL,
  `zip_code` varchar(6) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `sup_department_no` int DEFAULT NULL,
  `sup_serial_no` int DEFAULT NULL,
  PRIMARY KEY (`department_no`,`serial_no`),
  KEY `sup_department_no` (`sup_department_no`,`sup_serial_no`),
  FULLTEXT KEY `first_name` (`first_name`,`middle_name`,`surname`),
  CONSTRAINT `Employee_ibfk_1` FOREIGN KEY (`sup_department_no`, `sup_serial_no`) REFERENCES `Employee` (`department_no`, `serial_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee`
--

LOCK TABLES `Employee` WRITE;
/*!40000 ALTER TABLE `Employee` DISABLE KEYS */;
INSERT INTO `Employee` VALUES (12,1,'123409875678','2005-06-30','Srijan','Mohan','Aggrawal','srijan@gmail.com','N-10/63 D, Jawahar Nagar','567890','Noida','UP',NULL,NULL);
/*!40000 ALTER TABLE `Employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee_Age`
--

DROP TABLE IF EXISTS `Employee_Age`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee_Age` (
  `age` int NOT NULL,
  `employee_serial_no` int NOT NULL,
  `employee_department_no` int NOT NULL,
  PRIMARY KEY (`age`,`employee_serial_no`,`employee_department_no`),
  KEY `employee_department_no` (`employee_department_no`,`employee_serial_no`),
  CONSTRAINT `Employee_Age_ibfk_1` FOREIGN KEY (`employee_department_no`, `employee_serial_no`) REFERENCES `Employee` (`department_no`, `serial_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee_Age`
--

LOCK TABLES `Employee_Age` WRITE;
/*!40000 ALTER TABLE `Employee_Age` DISABLE KEYS */;
INSERT INTO `Employee_Age` VALUES (15,1,12);
/*!40000 ALTER TABLE `Employee_Age` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee_Contact`
--

DROP TABLE IF EXISTS `Employee_Contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee_Contact` (
  `contact_number` varchar(15) NOT NULL,
  `employee_serial_no` int NOT NULL,
  `employee_department_no` int NOT NULL,
  PRIMARY KEY (`contact_number`,`employee_serial_no`,`employee_department_no`),
  KEY `employee_department_no` (`employee_department_no`,`employee_serial_no`),
  CONSTRAINT `Employee_Contact_ibfk_1` FOREIGN KEY (`employee_department_no`, `employee_serial_no`) REFERENCES `Employee` (`department_no`, `serial_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee_Contact`
--

LOCK TABLES `Employee_Contact` WRITE;
/*!40000 ALTER TABLE `Employee_Contact` DISABLE KEYS */;
/*!40000 ALTER TABLE `Employee_Contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee_Dependant`
--

DROP TABLE IF EXISTS `Employee_Dependant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee_Dependant` (
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `date_of_birth` date NOT NULL,
  PRIMARY KEY (`first_name`,`middle_name`,`surname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee_Dependant`
--

LOCK TABLES `Employee_Dependant` WRITE;
/*!40000 ALTER TABLE `Employee_Dependant` DISABLE KEYS */;
INSERT INTO `Employee_Dependant` VALUES ('Amit','M','Aggrawal','2005-06-29');
/*!40000 ALTER TABLE `Employee_Dependant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee_Dependant_Age`
--

DROP TABLE IF EXISTS `Employee_Dependant_Age`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee_Dependant_Age` (
  `age` int NOT NULL,
  `dependant_first_name` varchar(50) NOT NULL,
  `dependant_middle_name` varchar(50) NOT NULL,
  `dependant_surname` varchar(50) NOT NULL,
  PRIMARY KEY (`age`,`dependant_first_name`,`dependant_middle_name`,`dependant_surname`),
  KEY `dependant_first_name` (`dependant_first_name`,`dependant_middle_name`,`dependant_surname`),
  CONSTRAINT `Employee_Dependant_Age_ibfk_1` FOREIGN KEY (`dependant_first_name`, `dependant_middle_name`, `dependant_surname`) REFERENCES `Employee_Dependant` (`first_name`, `middle_name`, `surname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee_Dependant_Age`
--

LOCK TABLES `Employee_Dependant_Age` WRITE;
/*!40000 ALTER TABLE `Employee_Dependant_Age` DISABLE KEYS */;
INSERT INTO `Employee_Dependant_Age` VALUES (15,'Amit','M','Aggrawal');
/*!40000 ALTER TABLE `Employee_Dependant_Age` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `House`
--

DROP TABLE IF EXISTS `House`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `House` (
  `policy_id` varchar(15) NOT NULL,
  `replacement_cost` decimal(18,2) NOT NULL,
  `street_address` varchar(100) NOT NULL,
  `zip_code` varchar(6) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  PRIMARY KEY (`policy_id`),
  CONSTRAINT `House_ibfk_1` FOREIGN KEY (`policy_id`) REFERENCES `Policy` (`policy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `House`
--

LOCK TABLES `House` WRITE;
/*!40000 ALTER TABLE `House` DISABLE KEYS */;
INSERT INTO `House` VALUES ('hous#345678',200000.00,'iiith nagar','456789','Noida ','UP');
/*!40000 ALTER TABLE `House` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Life`
--

DROP TABLE IF EXISTS `Life`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Life` (
  `policy_id` varchar(15) NOT NULL,
  `death_value_benefit` decimal(18,2) NOT NULL,
  `medical_history` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`policy_id`),
  CONSTRAINT `Life_ibfk_1` FOREIGN KEY (`policy_id`) REFERENCES `Policy` (`policy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Life`
--

LOCK TABLES `Life` WRITE;
/*!40000 ALTER TABLE `Life` DISABLE KEYS */;
INSERT INTO `Life` VALUES ('Life#234567',300000.00,'healthy. - fit.');
/*!40000 ALTER TABLE `Life` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Medical`
--

DROP TABLE IF EXISTS `Medical`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Medical` (
  `policy_id` varchar(15) NOT NULL,
  `death_value_benefit` decimal(18,2) NOT NULL,
  PRIMARY KEY (`policy_id`),
  CONSTRAINT `Medical_ibfk_1` FOREIGN KEY (`policy_id`) REFERENCES `Policy` (`policy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Medical`
--

LOCK TABLES `Medical` WRITE;
/*!40000 ALTER TABLE `Medical` DISABLE KEYS */;
INSERT INTO `Medical` VALUES ('medi#123456',300000.00);
/*!40000 ALTER TABLE `Medical` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Policy`
--

DROP TABLE IF EXISTS `Policy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Policy` (
  `policy_id` varchar(15) NOT NULL,
  `terms_and_conditions` varchar(1000) DEFAULT NULL,
  `date_of_issue` date NOT NULL,
  `durantion_in_months` int NOT NULL,
  `premium_value` decimal(18,2) NOT NULL,
  `sum_assured` decimal(18,2) NOT NULL,
  `customer_aadhar_no` varchar(20) NOT NULL,
  `employee_department_no` int NOT NULL,
  `employee_serial_no` int NOT NULL,
  PRIMARY KEY (`policy_id`),
  KEY `customer_aadhar_no` (`customer_aadhar_no`),
  KEY `employee_department_no` (`employee_department_no`,`employee_serial_no`),
  CONSTRAINT `Policy_ibfk_1` FOREIGN KEY (`customer_aadhar_no`) REFERENCES `Customer` (`aadhar_no`),
  CONSTRAINT `Policy_ibfk_2` FOREIGN KEY (`employee_department_no`, `employee_serial_no`) REFERENCES `Employee` (`department_no`, `serial_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Policy`
--

LOCK TABLES `Policy` WRITE;
/*!40000 ALTER TABLE `Policy` DISABLE KEYS */;
INSERT INTO `Policy` VALUES ('hous#345678','its regular policy','2007-07-07',12,3000.00,300000.00,'567812340987',12,1),('Life#234567','it is a regular policy. - it cannot be transferred to anyone.','2007-07-07',12,3000.00,300000.00,'567812340987',12,1),('medi#123456','its regular policy.','2007-07-07',12,3000.00,300000.00,'567812340987',12,1),('trav#975369','its regular travel policy','2007-07-07',12,3000.00,300000.00,'567812340987',12,1),('vehi#570852','its regular vehicle policy.- it cannot be transferred','2007-07-07',12,3000.00,300000.00,'567812340987',12,1);
/*!40000 ALTER TABLE `Policy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Provided_By`
--

DROP TABLE IF EXISTS `Provided_By`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Provided_By` (
  `employee_department_no` int NOT NULL,
  `employee_serial_no` int NOT NULL,
  `dependant_first_name` varchar(50) NOT NULL,
  `dependant_middle_name` varchar(50) NOT NULL,
  `dependant_surname` varchar(50) NOT NULL,
  PRIMARY KEY (`employee_department_no`,`employee_serial_no`,`dependant_first_name`,`dependant_middle_name`,`dependant_surname`),
  KEY `dependant_first_name` (`dependant_first_name`,`dependant_middle_name`,`dependant_surname`),
  CONSTRAINT `Provided_By_ibfk_1` FOREIGN KEY (`employee_department_no`, `employee_serial_no`) REFERENCES `Employee` (`department_no`, `serial_no`),
  CONSTRAINT `Provided_By_ibfk_2` FOREIGN KEY (`dependant_first_name`, `dependant_middle_name`, `dependant_surname`) REFERENCES `Employee_Dependant` (`first_name`, `middle_name`, `surname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Provided_By`
--

LOCK TABLES `Provided_By` WRITE;
/*!40000 ALTER TABLE `Provided_By` DISABLE KEYS */;
INSERT INTO `Provided_By` VALUES (12,1,'Amit','M','Aggrawal');
/*!40000 ALTER TABLE `Provided_By` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Resolves_Claims`
--

DROP TABLE IF EXISTS `Resolves_Claims`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Resolves_Claims` (
  `TPA_id` varchar(20) NOT NULL,
  `employee_department_no` int NOT NULL,
  `employee_serial_no` int NOT NULL,
  `policy_id` varchar(15) NOT NULL,
  `customer_aadhar_no` varchar(20) NOT NULL,
  PRIMARY KEY (`TPA_id`,`employee_department_no`,`employee_serial_no`,`policy_id`,`customer_aadhar_no`),
  KEY `employee_department_no` (`employee_department_no`,`employee_serial_no`),
  KEY `policy_id` (`policy_id`),
  KEY `customer_aadhar_no` (`customer_aadhar_no`),
  CONSTRAINT `Resolves_Claims_ibfk_1` FOREIGN KEY (`TPA_id`) REFERENCES `TPA` (`TPA_id`),
  CONSTRAINT `Resolves_Claims_ibfk_2` FOREIGN KEY (`employee_department_no`, `employee_serial_no`) REFERENCES `Employee` (`department_no`, `serial_no`),
  CONSTRAINT `Resolves_Claims_ibfk_3` FOREIGN KEY (`policy_id`) REFERENCES `Policy` (`policy_id`),
  CONSTRAINT `Resolves_Claims_ibfk_4` FOREIGN KEY (`customer_aadhar_no`) REFERENCES `Customer` (`aadhar_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Resolves_Claims`
--

LOCK TABLES `Resolves_Claims` WRITE;
/*!40000 ALTER TABLE `Resolves_Claims` DISABLE KEYS */;
INSERT INTO `Resolves_Claims` VALUES ('5678-9853',12,1,'hous#345678','567812340987');
/*!40000 ALTER TABLE `Resolves_Claims` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TPA`
--

DROP TABLE IF EXISTS `TPA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TPA` (
  `TPA_id` varchar(20) NOT NULL,
  `TPA_name` varchar(50) NOT NULL,
  `street_address` varchar(100) NOT NULL,
  `zip_code` varchar(6) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  PRIMARY KEY (`TPA_id`),
  FULLTEXT KEY `TPA_name` (`TPA_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TPA`
--

LOCK TABLES `TPA` WRITE;
/*!40000 ALTER TABLE `TPA` DISABLE KEYS */;
INSERT INTO `TPA` VALUES ('5678-9853','NRC','N-12/64 D, Rajiv Gandhi Nagar','369649','Noida','UP');
/*!40000 ALTER TABLE `TPA` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TPA_Contact_Info`
--

DROP TABLE IF EXISTS `TPA_Contact_Info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TPA_Contact_Info` (
  `contact_number` varchar(15) NOT NULL,
  `TPA_id` varchar(20) NOT NULL,
  PRIMARY KEY (`contact_number`,`TPA_id`),
  KEY `TPA_id` (`TPA_id`),
  CONSTRAINT `TPA_Contact_Info_ibfk_1` FOREIGN KEY (`TPA_id`) REFERENCES `TPA` (`TPA_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TPA_Contact_Info`
--

LOCK TABLES `TPA_Contact_Info` WRITE;
/*!40000 ALTER TABLE `TPA_Contact_Info` DISABLE KEYS */;
INSERT INTO `TPA_Contact_Info` VALUES ('9026816423','5678-9853'),('9026816426','5678-9853');
/*!40000 ALTER TABLE `TPA_Contact_Info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TPA_Investigations_Conducted`
--

DROP TABLE IF EXISTS `TPA_Investigations_Conducted`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TPA_Investigations_Conducted` (
  `type` varchar(30) NOT NULL,
  `TPA_id` varchar(20) NOT NULL,
  PRIMARY KEY (`type`,`TPA_id`),
  KEY `TPA_id` (`TPA_id`),
  CONSTRAINT `TPA_Investigations_Conducted_ibfk_1` FOREIGN KEY (`TPA_id`) REFERENCES `TPA` (`TPA_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TPA_Investigations_Conducted`
--

LOCK TABLES `TPA_Investigations_Conducted` WRITE;
/*!40000 ALTER TABLE `TPA_Investigations_Conducted` DISABLE KEYS */;
INSERT INTO `TPA_Investigations_Conducted` VALUES ('drug-overdose','5678-9853'),('smuggling','5678-9853');
/*!40000 ALTER TABLE `TPA_Investigations_Conducted` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Travel`
--

DROP TABLE IF EXISTS `Travel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Travel` (
  `policy_id` varchar(15) NOT NULL,
  `itenerary` varchar(1000) DEFAULT NULL,
  `airline_and_hotel_bookings` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`policy_id`),
  CONSTRAINT `Travel_ibfk_1` FOREIGN KEY (`policy_id`) REFERENCES `Policy` (`policy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Travel`
--

LOCK TABLES `Travel` WRITE;
/*!40000 ALTER TABLE `Travel` DISABLE KEYS */;
INSERT INTO `Travel` VALUES ('trav#975369','Visit India Gate. Eat at Leopold Cafe.','Indigo, Hotel Taj');
/*!40000 ALTER TABLE `Travel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Travel_Destinations`
--

DROP TABLE IF EXISTS `Travel_Destinations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Travel_Destinations` (
  `policy_id` varchar(15) NOT NULL,
  `destination` varchar(20) NOT NULL,
  PRIMARY KEY (`policy_id`,`destination`),
  CONSTRAINT `Travel_Destinations_ibfk_1` FOREIGN KEY (`policy_id`) REFERENCES `Travel` (`policy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Travel_Destinations`
--

LOCK TABLES `Travel_Destinations` WRITE;
/*!40000 ALTER TABLE `Travel_Destinations` DISABLE KEYS */;
INSERT INTO `Travel_Destinations` VALUES ('trav#975369','Delhi'),('trav#975369','Hyderabad'),('trav#975369','Mumbai');
/*!40000 ALTER TABLE `Travel_Destinations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Vehicle`
--

DROP TABLE IF EXISTS `Vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Vehicle` (
  `policy_id` varchar(15) NOT NULL,
  `license_plate_no` varchar(12) NOT NULL,
  PRIMARY KEY (`policy_id`),
  CONSTRAINT `Vehicle_ibfk_1` FOREIGN KEY (`policy_id`) REFERENCES `Policy` (`policy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Vehicle`
--

LOCK TABLES `Vehicle` WRITE;
/*!40000 ALTER TABLE `Vehicle` DISABLE KEYS */;
INSERT INTO `Vehicle` VALUES ('vehi#570852','MH01KL5164');
/*!40000 ALTER TABLE `Vehicle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Vehicle_Colours`
--

DROP TABLE IF EXISTS `Vehicle_Colours`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Vehicle_Colours` (
  `policy_id` varchar(15) NOT NULL,
  `colour` varchar(20) NOT NULL,
  PRIMARY KEY (`policy_id`,`colour`),
  CONSTRAINT `Vehicle_Colours_ibfk_1` FOREIGN KEY (`policy_id`) REFERENCES `Vehicle` (`policy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Vehicle_Colours`
--

LOCK TABLES `Vehicle_Colours` WRITE;
/*!40000 ALTER TABLE `Vehicle_Colours` DISABLE KEYS */;
INSERT INTO `Vehicle_Colours` VALUES ('vehi#570852','blue'),('vehi#570852','green');
/*!40000 ALTER TABLE `Vehicle_Colours` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-24 20:25:24
