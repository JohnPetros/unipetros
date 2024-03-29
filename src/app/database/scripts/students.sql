-- Active: 1711212961472@@127.0.0.1@3306@unipetros
DROP TABLE IF EXISTS students;

CREATE TABLE students (
  id CHAR(36) DEFAULT (uuid()) PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL, 
  phone CHAR(11) NOT NULL, 
  avatar VARCHAR(255) DEFAULT 'default-avatar.png',
  birthdate DATE NOT NULL,
  gender ENUM('male', 'female'),
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  course_id CHAR(36),
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
);

INSERT INTO students (name, email, password, phone, birthdate, gender, course_id)
VALUES
('Lúcia Romena', 'lucia300@unipetros.com', '$2b$12$WrntejsV/WPVXRfM0EFPy.X6nvy1UCwNTgPDCmayvYfhsVANRxGo.', '12894561235', '2002-03-16', 'female', '01cbf711-ec80-11ee-8ced-0242ac130002'),
('Milena Oliveira', 'milena7777@unipetros.com', '$2b$12$WrntejsV/WPVXRfM0EFPy.X6nvy1UCwNTgPDCmayvYfhsVANRxGo.', '21456789632', '2005-08-15', 'female', '01cd80a7-ec80-11ee-8ced-0242ac130002'),
('Raquel Oliveira', 'milena8888@unipetros.com', '$2b$12$WrntejsV/WPVXRfM0EFPy.X6nvy1UCwNTgPDCmayvYfhsVANRxGo.', '22456789635', '2006-11-12', 'female', '01cdc9fe-ec80-11ee-8ced-0242ac130002');

DELETE FROM students;

SELECT * FROM students;

SELECT 
  S.*, 
  C.name AS course_name
FROM students AS S
JOIN courses AS C ON C.id = S.course_id
GROUP BY S.id

SELECT gender, COUNT(gender) AS count
FROM students
GROUP BY gender;