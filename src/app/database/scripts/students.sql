-- Active: 1712242301041@@127.0.0.1@3306@unipetros
DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS students (
  id CHAR(36) DEFAULT (uuid()) PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL, 
  phone CHAR(11) NOT NULL, 
  avatar VARCHAR(255) DEFAULT 'default-avatar.png',
  birthdate DATE NOT NULL,
  gender ENUM('male', 'female'),
  created_at TIMESTAMP NOT NULL DEFAULT (UTC_TIMESTAMP),
  course_id CHAR(36) NOT NULL,
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
);

ALTER TABLE students ADD COLUMN is_active BOOLEAN DEFAULT 1 NOT NULL;

ALTER TABLE students DROP COLUMN is_active;

INSERT INTO students (name, email, password, phone, birthdate, gender, course_id)
VALUES
('Jefferson Henrique', 'jefferson@unipetros.com', '$2b$12$WrntejsV/WPVXRfM0EFPy.X6nvy1UCwNTgPDCmayvYfhsVANRxGo.', '22456789635', '2006-11-12', 'male', '2a0752da-f65d-11ee-b82f-0242ac140002');

DELETE FROM students;

SELECT * FROM students;

SELECT 
  S.*, 
  C.name AS course_name,
  (SELECT EXISTS (
    SELECT 1 
    FROM students_dismissals AS SD 
    WHERE SD.student_id = S.id
  )) AS is_active
FROM students AS S
JOIN courses AS C ON C.id = S.course_id
GROUP BY S.id

SELECT gender, COUNT(gender) AS count
FROM students
GROUP BY gender;

SELECT 
  S.*, 
  GROUP_CONCAT(C.name) AS course_name,
  (SELECT EXISTS (
    SELECT 1 
    FROM students_dismissals AS SD 
    WHERE SD.student_id = S.id
  )) AS is_active
FROM students AS S
JOIN courses AS C ON C.id = S.course_id
GROUP BY S.id
ORDER BY S.created_at DESC
LIMIT 4;
