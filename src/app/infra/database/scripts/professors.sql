-- Active: 1712190283212@@localhost@3306@unipetros
USE unipetros;

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

DELETE FROM professors;

SELECT * FROM professors;

SELECT COUNT(id) AS count FROM professors


SELECT 
  P.*, 
  GROUP_CONCAT(S.id) AS subjects_ids, 
  GROUP_CONCAT(S.name) AS subjects_names
FROM professors AS P
LEFT JOIN professors_subjects AS PS ON PS.professor_id = P.id 
LEFT JOIN subjects AS S ON PS.subject_id = S.id
WHERE P.name LIKE '%felix%' OR P.email LIKE '%felix.nc@gmail.com%'
GROUP BY P.id