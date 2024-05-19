-- Active: 1715824547022@@127.0.0.1@3306@unipetros
DROP TABLE IF EXISTS students_absents;

CREATE TABLE IF NOT EXISTS students_absents (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY,
  date DATE DEFAULT (CURDATE()) NOT NULL,
  student_id CHAR(36) NOT NULL,
  FOREIGN KEY students_absents(student_id) REFERENCES students(id) ON DELETE CASCADE
);

INSERT INTO students_absents (student_id, date) VALUES
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-03-29'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-03-28'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-03-27'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-03-26'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-02-12'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-02-25'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-03-16'),
('73e3c397-7c5c-406d-a45a-82642bd4b6cb', '2024-03-16'),
('39bee53f-4d2b-4f11-b861-28c3934a77f7', '2024-03-16'),
('39bee53f-4d2b-4f11-b861-28c3934a77f7', '2024-03-17'),
('39bee53f-4d2b-4f11-b861-28c3934a77f7', '2024-02-17'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-03-20'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-03-21'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-03-03'),
('39bee53f-4d2b-4f11-b861-28c3934a77f7', '2024-03-15'),
('39bee53f-4d2b-4f11-b861-28c3934a77f7', '2024-03-29'),
('73e3c397-7c5c-406d-a45a-82642bd4b6cb', '2024-03-30'),
('73e3c397-7c5c-406d-a45a-82642bd4b6cb', '2024-02-12'),
('73e3c397-7c5c-406d-a45a-82642bd4b6cb', '2024-03-10'),
('73e3c397-7c5c-406d-a45a-82642bd4b6cb', '2024-03-28'),
('73e3c397-7c5c-406d-a45a-82642bd4b6cb', '2024-03-24'),
('73e3c397-7c5c-406d-a45a-82642bd4b6cb', '2024-03-26'),
('73e3c397-7c5c-406d-a45a-82642bd4b6cb', '2024-03-21');

DELETE FROM students_absents;

SELECT * FROM students_absents;
