-- Active: 1715824547022@@127.0.0.1@3306@unipetros
DROP TABLE IF EXISTS students_dismissals;

CREATE TABLE IF NOT EXISTS students_dismissals (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY,
  date DATE NOT NULL,
  student_id CHAR(36) NOT NULL,
  FOREIGN KEY students_dismissals(student_id) REFERENCES students(id) ON DELETE CASCADE
);

INSERT INTO students_dismissals (student_id, date) VALUES
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-05-08'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-05-18'),
('9cf193f7-ec8e-488b-8d0e-3ed9fb144f77', '2024-05-17'),
('9cf193f7-ec8e-488b-8d0e-3ed9fb144f77', '2024-05-16'),
('9cf193f7-ec8e-488b-8d0e-3ed9fb144f77', '2024-02-12'),
('9cf193f7-ec8e-488b-8d0e-3ed9fb144f77', '2024-02-15'),
('9cf193f7-ec8e-488b-8d0e-3ed9fb144f77', '2024-05-17'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-02-17'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-05-10'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-05-11'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-05-05'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-05-15'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-05-09');

DELETE FROM students_dismissals;

SELECT * FROM students_dismissals;
