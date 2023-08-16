-- Script that creates the table id_not_null on your MySQL server.
CREATE TABLE IF NOT EXISTS id_not_null(
	ID INT DEFAULT 1,
	name VARCHAR(256)
);