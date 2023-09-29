SHOW DATABASES;
CREATE DATABASE `test1`;
USE `test1`;
SELECT DATABASE();

SHOW TABLES;

show columns from `student`;

select * from `student1`;

INSERT INTO `student1` VALUES(1,"小白",23,'2000-2-20');
INSERT INTO `student1` VALUES(2,"小黃",22,'2000-3-05');
INSERT INTO `student1` VALUES(3,"小藍",24,'2000-2-10');

UPDATE `student1` SET Birthday = '1999-06-20' WHERE Birthday = '2000-02-10';

COMMIT;