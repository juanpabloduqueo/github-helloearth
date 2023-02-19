-- MariaDB dump 10.19  Distrib 10.6.11-MariaDB, for Linux (x86_64)
--
-- Host: classmysql.engr.oregonstate.edu    Database: cs340_duqueocj
-- ------------------------------------------------------
-- Server version	10.6.11-MariaDB-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Locations`
--

DROP TABLE IF EXISTS `Locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Locations` (
  `locationId` int(11) NOT NULL AUTO_INCREMENT,
  `locationName` varchar(45) NOT NULL,
  `address` varchar(255) NOT NULL,
  `zipcode` varchar(45) NOT NULL,
  `state` varchar(45) NOT NULL,
  `isClientLocation` tinyint(4) NOT NULL,
  PRIMARY KEY (`locationId`),
  UNIQUE KEY `locationId` (`locationId`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Locations`
--

LOCK TABLES `Locations` WRITE;
/*!40000 ALTER TABLE `Locations` DISABLE KEYS */;
INSERT INTO `Locations` VALUES (1,'HelloEarth Depot 1','123 Main Street','12345','State A',0),(2,'HelloEarth Depot 2','456 Market Ave','67890','State B',0),(3,'HelloEarth Depot 3','789 Ocean Blvd','24680','State C',0),(4,'Client Site 1','725 Oakland Blvd','24559','State C',1),(5,'Client Site 2','865 Park Ave','25683','State E',1),(6,'Client Site 3','325 Sunrise Blvd','24735','State F',1),(7,'Client Site 4','286 Market St','24750','State T',1);
/*!40000 ALTER TABLE `Locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Machines`
--

DROP TABLE IF EXISTS `Machines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Machines` (
  `machineId` int(11) NOT NULL AUTO_INCREMENT,
  `year` year(4) NOT NULL,
  `make` varchar(45) NOT NULL,
  `model` varchar(45) NOT NULL,
  `serial` varchar(255) NOT NULL,
  `class` varchar(45) NOT NULL,
  PRIMARY KEY (`machineId`),
  UNIQUE KEY `machineId` (`machineId`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Machines`
--

LOCK TABLES `Machines` WRITE;
/*!40000 ALTER TABLE `Machines` DISABLE KEYS */;
INSERT INTO `Machines` VALUES (1,2010,'Liebherr','R 317 Litronic','1042-48528','Tracked Excavator'),(2,2017,'KOMATSU','HD325-8','50027','Off-Highway Truck'),(3,2020,'CATERPILLAR','963K','D8T49943','Tracked Loader'),(4,2001,'CATERPILLAR','D6M','3WN02456','Bulldozer'),(5,2001,'CATERPILLAR','320C','AKH01920','Tracked Excavator'),(6,2008,'CATERPILLAR','320DL','KGF02672','Tracked Excavator'),(7,2008,'INGERSOLL-RAND','SD70','168762','Compactor'),(8,1980,'CATERPILLAR','D6D','4X05964','Bulldozer'),(9,1982,'CATERPILLAR','D6D','75W02070','Bulldozer');
/*!40000 ALTER TABLE `Machines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Mechanics`
--

DROP TABLE IF EXISTS `Mechanics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Mechanics` (
  `mechanicId` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) NOT NULL,
  `phone` varchar(25) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`mechanicId`),
  UNIQUE KEY `mechanicId` (`mechanicId`),
  UNIQUE KEY `full_name` (`firstName`,`lastName`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Mechanics`
--

LOCK TABLES `Mechanics` WRITE;
/*!40000 ALTER TABLE `Mechanics` DISABLE KEYS */;
INSERT INTO `Mechanics` VALUES (1,'Bryan','Cook','+16945702087','bryan.cook@gmail.com'),(2,'Maverick','Ruiz','+1-432-416-1915','maverick.ruiz@gmail.com'),(3,'Clark','Bennet','(742) 757-1004 4662','clark.bennet@gmail.com'),(4,'John','Williams','(962) 857-1021 4889','johnhappy@hotmail.com'),(5,'Adam','Edison','(956)320-1080 4335','edisonjr@outlook.com'),(6,'Robert','Schalke','645-867-5309 5309','robschal@yahoo.com');
/*!40000 ALTER TABLE `Mechanics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Products`
--

DROP TABLE IF EXISTS `Products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Products` (
  `productId` int(11) NOT NULL AUTO_INCREMENT,
  `productName` varchar(45) NOT NULL,
  `reference` varchar(45) NOT NULL,
  `brand` varchar(45) NOT NULL,
  `description` text DEFAULT NULL,
  PRIMARY KEY (`productId`),
  UNIQUE KEY `productId` (`productId`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Products`
--

LOCK TABLES `Products` WRITE;
/*!40000 ALTER TABLE `Products` DISABLE KEYS */;
INSERT INTO `Products` VALUES (1,'Lubricant X','REF001','Brand A','High-quality lubricant for earth moving machinery'),(2,'Grease Y','REF002','Brand B','Special grease for heavy-duty earth moving equipment'),(3,'Spare Part Z','REF003','Brand C','Genuine spare part for earth moving machinery maintenance'),(4,'Hydraulic filter','P164381','Donaldson','Hydraulic filter for compactors'),(5,'Fuel filter','P551315','Donaldson','Fuel filter for excavators and bulldozers'),(6,'Air filter','P532501','Donaldson','Air filter for excavators'),(7,'Hydraulic oil','HYDO10','Caterpillar','Hydraulic oil 6000+ hours extended life'),(8,'Motor oil','15W40','Gulf','Motor multigrade oil');
/*!40000 ALTER TABLE `Products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WorkOrderMechanics`
--

DROP TABLE IF EXISTS `WorkOrderMechanics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `WorkOrderMechanics` (
  `workOrderMechanicId` int(11) NOT NULL AUTO_INCREMENT,
  `workOrderId` int(11) NOT NULL,
  `mechanicId` int(11) DEFAULT NULL,
  PRIMARY KEY (`workOrderMechanicId`),
  KEY `mechanicId` (`mechanicId`),
  KEY `workOrderId` (`workOrderId`),
  CONSTRAINT `WorkOrderMechanics_ibfk_1` FOREIGN KEY (`mechanicId`) REFERENCES `Mechanics` (`mechanicId`) ON DELETE SET NULL,
  CONSTRAINT `WorkOrderMechanics_ibfk_2` FOREIGN KEY (`workOrderId`) REFERENCES `WorkOrders` (`workOrderId`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WorkOrderMechanics`
--

LOCK TABLES `WorkOrderMechanics` WRITE;
/*!40000 ALTER TABLE `WorkOrderMechanics` DISABLE KEYS */;
INSERT INTO `WorkOrderMechanics` VALUES (1,1,1),(2,2,3),(3,3,1),(4,3,3),(5,4,2),(6,9,3),(7,7,6);
/*!40000 ALTER TABLE `WorkOrderMechanics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WorkOrderProducts`
--

DROP TABLE IF EXISTS `WorkOrderProducts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `WorkOrderProducts` (
  `workOrderProductId` int(11) NOT NULL AUTO_INCREMENT,
  `workOrderId` int(11) NOT NULL,
  `productId` int(11) DEFAULT NULL,
  PRIMARY KEY (`workOrderProductId`),
  KEY `productId` (`productId`),
  KEY `workOrderId` (`workOrderId`),
  CONSTRAINT `WorkOrderProducts_ibfk_1` FOREIGN KEY (`productId`) REFERENCES `Products` (`productId`) ON DELETE SET NULL,
  CONSTRAINT `WorkOrderProducts_ibfk_2` FOREIGN KEY (`workOrderId`) REFERENCES `WorkOrders` (`workOrderId`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WorkOrderProducts`
--

LOCK TABLES `WorkOrderProducts` WRITE;
/*!40000 ALTER TABLE `WorkOrderProducts` DISABLE KEYS */;
INSERT INTO `WorkOrderProducts` VALUES (1,1,1),(2,1,2),(3,2,1),(4,3,3),(5,4,3),(6,9,3),(7,7,7);
/*!40000 ALTER TABLE `WorkOrderProducts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WorkOrders`
--

DROP TABLE IF EXISTS `WorkOrders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `WorkOrders` (
  `workOrderId` int(11) NOT NULL AUTO_INCREMENT,
  `machineId` int(11) NOT NULL,
  `locationId` int(11) DEFAULT NULL,
  `date` date NOT NULL,
  `description` text DEFAULT NULL,
  PRIMARY KEY (`workOrderId`),
  UNIQUE KEY `workOrderId` (`workOrderId`),
  KEY `machineId` (`machineId`),
  KEY `locationId` (`locationId`),
  CONSTRAINT `WorkOrders_ibfk_1` FOREIGN KEY (`machineId`) REFERENCES `Machines` (`machineId`) ON DELETE CASCADE,
  CONSTRAINT `WorkOrders_ibfk_2` FOREIGN KEY (`locationId`) REFERENCES `Locations` (`locationId`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WorkOrders`
--

LOCK TABLES `WorkOrders` WRITE;
/*!40000 ALTER TABLE `WorkOrders` DISABLE KEYS */;
INSERT INTO `WorkOrders` VALUES (1,1,4,'2023-02-07','Machine needs a general check-up'),(2,3,1,'2023-02-07','Machine needs an oil change'),(3,1,2,'2023-02-08','Machine needs a new alternator'),(4,2,4,'2023-02-08','Machine needs a new starter'),(5,4,5,'2023-02-02','Perform 250-hour routine maintenance'),(6,5,6,'2023-01-20','Perform 1000-hour routine maintenance'),(7,8,3,'2023-01-15','Fix undercarriage issues'),(8,6,3,'2023-01-03','Adjust boom'),(9,7,7,'2022-12-15','Replace drum mounting pads');
/*!40000 ALTER TABLE `WorkOrders` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-19 13:00:24
