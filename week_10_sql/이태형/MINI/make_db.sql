
CREATE DATABASE place;
USE place;
CREATE TABLE `cafe` (
   `c_name` VARCHAR(50) PRIMARY KEY,
   `c_star` FLOAT,
   `c_address` TEXT,
   `c_latitude` FLOAT,
   `c_longitude` FLOAT
)
;
#BLOB


CREATE TABLE `entertain` (
   `e_name` VARCHAR(50) PRIMARY KEY,
   `e_address` TEXT,
   `e_latitude` FLOAT,
   `e_longitude` FLOAT
)
;

CREATE TABLE `emotion` (
   `em_name` VARCHAR(50) PRIMARY KEY,
   `blog_content` TEXT,
   `hash_content` TEXT,
   `href` TEXT
)

;

CREATE TABLE `restaurant` (
   `r_name` VARCHAR(50) PRIMARY KEY,
   `r_star` FLOAT,
   `r_address` TEXT,
   `r_latitude` FLOAT,
   `r_longitude` FLOAT 
)
;
