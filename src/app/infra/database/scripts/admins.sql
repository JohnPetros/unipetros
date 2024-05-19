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
(
  '5e557037-e936-11ee-b9aa-0242ac130002',
  'John Petros', 
  'john@unipetros.com',
  '$2b$12$WrntejsV/WPVXRfM0EFPy.X6nvy1UCwNTgPDCmayvYfhsVANRxGo.'
)

SELECT * FROM admins