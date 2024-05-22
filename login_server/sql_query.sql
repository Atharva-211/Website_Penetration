-- Log in to MySQL as root
-- Command: mysql -u root -p

-- Create the database
CREATE DATABASE atharva;

-- Use the created database
USE atharva;

-- Create the User table
CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(528) NOT NULL
);
