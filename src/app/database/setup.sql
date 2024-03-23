-- Active: 1711075081714@@127.0.0.1@3306@unipetros
DROP DATABASE IF EXISTS unipetros;
CREATE DATABASE IF NOT EXISTS unipetros;

USE unipetros;

DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
  id CHAR(36) DEFAULT (uuid()) PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL, 
  avatar VARCHAR(255) DEFAULT 'default-avatar.png',
  role ENUM('admin', 'teacher', 'student')
);

INSERT INTO users (name, email, password, role) VALUES
('John Petros', 'john@unipetros.com', '$2b$12$WrntejsV/WPVXRfM0EFPy.X6nvy1UCwNTgPDCmayvYfhsVANRxGo.', 'admin')

SELECT * FROM users