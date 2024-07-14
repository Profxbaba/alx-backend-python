-- SQL script that creates a table users with the required specifications
-- Creates a table named users
-- Ensures id is an integer, never null, auto increment, and primary key
-- Ensures email is a string (255 characters), never null, and unique
-- Ensures name is a string (255 characters)
-- The script will not fail if the table already exists

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id)
);
