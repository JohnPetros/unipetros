-- Active: 1711212961472@@127.0.0.1@3306@unipetros
CREATE DATABASE IF NOT EXISTS unipetros;

USE unipetros;

DROP TABLE IF EXISTS admins;
CREATE TABLE IF NOT EXISTS admins (
  id CHAR(36) DEFAULT (uuid()) PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL, 
  avatar VARCHAR(255) DEFAULT 'default-avatar.png'
);

INSERT INTO admins (name, email, password) VALUES
('John Petros', 'john@unipetros.com', '$2b$12$WrntejsV/WPVXRfM0EFPy.X6nvy1UCwNTgPDCmayvYfhsVANRxGo.')

SELECT * FROM admins

SELECT UTC_DATE() As Result;

DROP TABLE IF EXISTS professors;
CREATE TABLE IF NOT EXISTS professors (
  id CHAR(36) DEFAULT (uuid()) PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL, 
  phone VARCHAR(255) NOT NULL, 
  birthdate DATE NOT NULL,
  avatar VARCHAR(255) DEFAULT 'default-avatar.png',
  gender ENUM('male', 'female')
);

INSERT INTO professors (name, email, password, phone, gender, birthdate) VALUES
('John Petros', 'john@unipetros.com', '$2b$12$WrntejsV/WPVXRfM0EFPy.X6nvy1UCwNTgPDCmayvYfhsVANRxGo.', '12123451234', 'male', '2002-03-16'),
('Jane Doe', 'jane@example.com', '$2b$12$WrntejsV/WPVXRfM0EFPy.X6nvy1UCwNTgPDCmayvYfhsVANRxGo.', '1234567890', 'female', '1995-04-20'),
('Bob Smith', 'bob@smith.com', '$2b$12$WrntejsV/WPVXRfM0EFPy.X6nvy1UCwNTgPDCmayvYfhsVANRxGo.', '0987654321', 'male', '1980-05-30');


SELECT * FROM professors

DROP TABLE IF EXISTS subjects;
CREATE TABLE IF NOT EXISTS subjects (
  id CHAR(36) DEFAULT (uuid()) PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE
);

INSERT INTO subjects (name) VALUES
('Mathematics'),
('Physics'),
('Chemistry'),
('Biology'),
('History');

SELECT * FROM subjects


DROP TABLE IF EXISTS professors_subjects;
CREATE TABLE IF NOT EXISTS professors_subjects (
  professor_id CHAR(36) NOT NULL,
  subject_id CHAR(36) NOT NULL,
  PRIMARY KEY (professor_id, subject_id),
  FOREIGN KEY (professor_id) REFERENCES professors(id) ON DELETE CASCADE,
  FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
);

INSERT INTO professors_subjects (professor_id, subject_id) VALUES
('b5e426b9-e93a-11ee-b9aa-0242ac130002', 'c86ba7d1-e93b-11ee-b9aa-0242ac130002'),
('b5e426b9-e93a-11ee-b9aa-0242ac130002', 'c86ba520-e93b-11ee-b9aa-0242ac130002'),
('b5e426b9-e93a-11ee-b9aa-0242ac130002', 'c86ba843-e93b-11ee-b9aa-0242ac130002'),
('ed0d310b-e93b-11ee-b9aa-0242ac130002', 'c86ba843-e93b-11ee-b9aa-0242ac130002'),
('ed0d6319-e93b-11ee-b9aa-0242ac130002', 'c86acfb0-e93b-11ee-b9aa-0242ac130002');

SELECT P.*, GROUP_CONCAT(S.name) AS subject_names
FROM professors AS P
LEFT JOIN professors_subjects AS PS ON PS.professor_id = P.id 
LEFT JOIN subjects AS S ON PS.subject_id = S.id
GROUP BY P.id
