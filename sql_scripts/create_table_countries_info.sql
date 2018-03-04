CREATE DATABASE IF NOT EXISTS `countries`;

CREATE TABLE `countries`.`countries_info` (
  `country` varchar(45) NOT NULL,
  `population` int(11) DEFAULT NULL,
  `yearly_change` int(11) DEFAULT NULL,
  `net_change` int(11) DEFAULT NULL,
  `density` int(11) DEFAULT NULL,
  `land_area_km` int(11) DEFAULT NULL,
  `migrants` int(11) DEFAULT NULL,
  `fert_rate` int(11) DEFAULT NULL,
  `med_age` int(11) DEFAULT NULL,
  `urban_pop` int(11) DEFAULT NULL,
  `world_share` int(11) DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `modified_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`country`),
  UNIQUE KEY `country_UNIQUE` (`country`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
