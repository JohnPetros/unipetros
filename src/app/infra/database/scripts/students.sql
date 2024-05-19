-- Active: 1715824547022@@127.0.0.1@3306@unipetros
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

DELETE FROM students;

INSERT INTO students (id, name, email, password, phone, avatar, birthdate, gender, course_id) VALUES
(
  '5b23d6aa-2f49-489a-be1d-427ef0b8d023',
  'Carlos Eduardo', 
  'carloseduardo@unipetros.com', 
  '$2b$12$rD0BBdCRlMr6xtlMgzw8K.KDtIcb0JmhA1IXwUkUZmqlpWqdWxOrO',
  '12987654321',
  'default-avatar.png',
  '1997-11-10',
  'male',
  '2024-05-18 23:34:20',
  '01cdc9fe-ec80-11ee-8ced-0242ac130002',
  '1'
),
(
  '9cf193f7-ec8e-488b-8d0e-3ed9fb144f77',
  'Maria Fernanda', 
  'mariafernanda@unipetros.com', 
  '$2b$12$CNGdUFM2GG86swcD1b6zUuBa554gdonBVjnGeL7JJy9l9lnnKH79.',
  '12987654321',
  'default-avatar.png',
  '1996-10-05',
  'female',
  '2024-03-29 23:34:20',
  '01cdc995-ec80-11ee-8ced-0242ac130002',
  '0'
),
(
  '9cf193f7-cc8e-488b-8d0e-3ed9fb144f77',
  'Jessie Kuhn', 
  'jessie@unipetros.com', 
  '$2b$12$CNGdUFM2GG86swcD1b6zUuBa554gdonBVjnGeL7JJy9l9lnnKH79.',
  '12987654321',
  'default-avatar.png',
  '1998-10-05',
  'male',
  '2024-05-09 23:34:20',
  '01cdc995-ec80-11ee-8ced-0242ac130002',
  '0'
),
(
  '9cf193f7-ac8e-488b-8d0e-3ed9fb144f77',
  'Erika Matthews', 
  'erika@unipetros.com', 
  '$2b$12$CNGdUFM2GG86swcD1b6zUuBa554gdonBVjnGeL7JJy9l9lnnKH79.',
  '12987654321',
  'default-avatar.png',
  '1990-10-05',
  'female',
  '2024-05-05 23:34:20',
  '01cdc9fe-ec80-11ee-8ced-0242ac130002',
  '0'
),
(
  '9cf193f7-ac8e-488b-8d0e-3ed9fb144f77',
  'Kurt Bishop', 
  'kurt@unipetros.com', 
  '$2b$12$CNGdUFM2GG86swcD1b6zUuBa554gdonBVjnGeL7JJy9l9lnnKH79.',
  '12987654321',
  'default-avatar.png',
  '1991-10-05',
  'male',
  '2024-05-05 23:34:20',
  '01cdc995-ec80-11ee-8ced-0242ac130002',
  '1'
),
(
  '9cf193f7-ac8e-488b-8d0e-3ed9fb144f77',
  'Tara Soto', 
  'tara@unipetros.com', 
  '$2b$12$CNGdUFM2GG86swcD1b6zUuBa554gdonBVjnGeL7JJy9l9lnnKH79.',
  '12987654321',
  'default-avatar.png',
  '1995-10-05',
  'female',
  '2024-05-15 23:34:20',
  '01cd80a7-ec80-11ee-8ced-0242ac130002',
  '1'
),
(
  '9cf193f7-bc8e-488b-8d0e-3ed9fb144f77',
  'George Phillips', 
  'erika@unipetros.com', 
  '$2b$12$CNGdUFM2GG86swcD1b6zUuBa554gdonBVjnGeL7JJy9l9lnnKH79.',
  '12987654321',
  'default-avatar.png',
  '1990-10-05',
  'female',
  '2024-05-05 23:34:20',
  '01cbf711-ec80-11ee-8ced-0242ac130002',
  '0'
),
(
  '73e3c397-7c5c-406d-a45a-82642bd4b6cb',
  'Sofia Martins', 
  'sofiamartins@unipetros.com',
  '$2b$12$v/UILFnxM1nq6WCgDCWFNuO1hBDNrVS9wVM0DSDjYki8ozgIhjR0S',
  '12987654321',
  'default-avatar.png',
  '1998-12-15',
  'female',
  '2024-03-29 23:34:20',
  '01cdca5b-ec80-11ee-8ced-0242ac130002',
  '1'
),
(
  '39bee53f-4d2b-4f11-b861-28c3934a77f7',
  'Rafael Santos', 
  'rafaelsantos@unipetros.com',
  '$2b$12$lFnNvUIvZ7rzUAalD6LsPee9ekugEItfWjmzm0ftG5ALAYFpqjSuq',
  '12987654321',
  'default-avatar.png',
  '1999-01-20',
  'male',
  '2024-03-29 23:34:20',
  '01cbf711-ec80-11ee-8ced-0242ac130002',
  '1'
);

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
