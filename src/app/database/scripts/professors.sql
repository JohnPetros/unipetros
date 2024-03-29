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

SELECT * FROM professors;

SELECT COUNT(id) AS count FROM professors

DELETE FROM professors;
