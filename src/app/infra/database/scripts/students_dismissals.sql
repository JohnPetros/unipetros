-- Active: 1712242301041@@127.0.0.1@3306@unipetros
DROP TABLE IF EXISTS students_dismissals;

CREATE TABLE IF NOT EXISTS students_dismissals (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY,
  date DATE NOT NULL,
  student_id CHAR(36) NOT NULL,
  FOREIGN KEY students_dismissals(student_id) REFERENCES students(id) ON DELETE CASCADE
);

INSERT INTO students_dismissals (student_id, date) VALUES
('9ad10acd-f65f-11ee-b82f-0242ac140002', '2024-03-29'),
('9ad10acd-f65f-11ee-b82f-0242ac140002', '2024-03-28'),
('9ad10ec2-f65f-11ee-b82f-0242ac140002', '2024-03-27'),
('9ad10ec2-f65f-11ee-b82f-0242ac140002', '2024-03-26'),
('9ad10ec2-f65f-11ee-b82f-0242ac140002', '2024-02-12'),
('9ad10ec2-f65f-11ee-b82f-0242ac140002', '2024-02-25'),
('9ad10ec2-f65f-11ee-b82f-0242ac140002', '2024-03-17'),
('9ad10acd-f65f-11ee-b82f-0242ac140002', '2024-02-17'),
('9ad10acd-f65f-11ee-b82f-0242ac140002', '2024-03-20'),
('9ad10acd-f65f-11ee-b82f-0242ac140002', '2024-03-21'),
('9ad10acd-f65f-11ee-b82f-0242ac140002', '2024-03-03'),
('9ad10acd-f65f-11ee-b82f-0242ac140002', '2024-03-15'),
('9ad10acd-f65f-11ee-b82f-0242ac140002', '2024-03-29');

DELETE FROM students_dismissals;

SELECT * FROM students_dismissals;
