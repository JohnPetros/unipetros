-- Active: 1711212961472@@127.0.0.1@3306
DROP TABLE IF EXISTS students_absents;

CREATE TABLE IF NOT EXISTS students_absents (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY,
  date DATE DEFAULT CURRENT_DATE NOT NULL,
  student_id CHAR(36) NOT NULL,
  FOREIGN KEY students_absents(student_id) REFERENCES students(id) ON DELETE CASCADE
);

INSERT INTO students_absents (student_id, date) VALUES
('21961378-0d00-435a-9fe5-f9579ae8715a', '2024-03-29'),
('21961378-0d00-435a-9fe5-f9579ae8715a', '2024-03-28'),
('21961378-0d00-435a-9fe5-f9579ae8715a', '2024-03-27'),
('21961378-0d00-435a-9fe5-f9579ae8715a', '2024-03-26'),
('21961378-0d00-435a-9fe5-f9579ae8715a', '2024-02-12'),
('21961378-0d00-435a-9fe5-f9579ae8715a', '2024-02-25'),
('21961378-0d00-435a-9fe5-f9579ae8715a', '2024-03-16'),
('32482290-be97-4fdd-8060-a087b37b6a6e', '2024-03-16'),
('39bee53f-4d2b-4f11-b861-28c3934a77f7', '2024-03-16'),
('39bee53f-4d2b-4f11-b861-28c3934a77f7', '2024-03-17'),
('39bee53f-4d2b-4f11-b861-28c3934a77f7', '2024-02-17'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-03-20'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-03-21'),
('5b23d6aa-2f49-489a-be1d-427ef0b8d023', '2024-03-03'),
('73e3c397-7c5c-406d-a45a-82642bd4b6cb', '2024-03-15'),
('73e3c397-7c5c-406d-a45a-82642bd4b6cb', '2024-03-29'),
('9cf193f7-ec8e-488b-8d0e-3ed9fb144f77', '2024-03-30'),
('9cf193f7-ec8e-488b-8d0e-3ed9fb144f77', '2024-02-12'),
('9cf193f7-ec8e-488b-8d0e-3ed9fb144f77', '2024-03-10'),
('9cf193f7-ec8e-488b-8d0e-3ed9fb144f77', '2024-03-28'),
('9cf193f7-ec8e-488b-8d0e-3ed9fb144f77', '2024-03-24'),
('9cf193f7-ec8e-488b-8d0e-3ed9fb144f77', '2024-03-26'),
('9cf193f7-ec8e-488b-8d0e-3ed9fb144f77', '2024-03-21'),
('fb4c6227-932a-47a2-97ca-f4942d13aeab', '2024-03-26'),
('fb4c6227-932a-47a2-97ca-f4942d13aeab', '2024-03-21');

DELETE FROM students_absents;

SELECT * FROM students_absents;
