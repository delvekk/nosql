USE LAB;

CREATE TABLE TEST_TABLE(
	ID INT NOT NULL auto_increment primary key,
	column1 INT NOT NULL,
	column2 INT NOT NULL,
	column3 INT NOT NULL,
	column4 INT NOT NULL,
	column5 VARCHAR(10) NOT NULL,
	column6 VARCHAR(10) NOT NULL,
	column7 INT NOT NULL,
	column8 INT NOT NULL,
	column9 INT NOT NULL);

drop procedure if exists insertRecords;
DELIMITER //
CREATE PROCEDURE insertRecords()
BEGIN
DECLARE i INT DEFAULT 1;
WHILE i <= 15000 DO
	INSERT INTO TEST_TABLE VALUES (i, i+1, i+2, i+3, i+4, 'ABC', 'ABC', i+5, i+6, i+7);
	SET i = i + 1;
END WHILE;
END; //

CALL insertRecords();