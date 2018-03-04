CREATE DATABASE IF NOT EXISTS `countries`;


CREATE TABLE `capital_cities` (
  `country_id` int(11) NOT NULL AUTO_INCREMENT,
  `country_name` varchar(100) NOT NULL,
  `capital_city` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`country_id`),
  UNIQUE KEY `country_name_UNIQUE` (`country_name`)
) ENGINE=InnoDB AUTO_INCREMENT=198 DEFAULT CHARSET=latin1;