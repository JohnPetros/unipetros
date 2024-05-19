-- Active: 1715824547022@@127.0.0.1@3306@unipetros
USE unipetros;

DROP TABLE IF EXISTS professors;

CREATE TABLE IF NOT EXISTS professors (
    id CHAR(36) DEFAULT(uuid()) PRIMARY KEY, 
    name VARCHAR(255) NOT NULL, 
    email VARCHAR(255) NOT NULL UNIQUE, password VARCHAR(255) NOT NULL, 
    phone VARCHAR(255) NOT NULL,
    birthdate DATE NOT NULL, 
    avatar VARCHAR(255) DEFAULT 'default-avatar.png', 
    gender ENUM('male', 'female')
);

INSERT INTO professors name, email, password, phone, gender, birthdate
VALUES 
(
    '062ac118-15de-46c8-974e-db33dfc46f38',
    'Jimmy Pinkman', 
    'jimmy@unipetros.com',
    '$2b$12$WrntejsV/WPVXRfM0EFPy.X6nvy1UCwNTgPDCmayvYfhsVANRxGo.', 
    '12123451234', 
    'male', 
    '2002-03-16'
),
(
    'd8e270de-509b-48dd-b485-5ec56cb2e55d',
    'Jane Doe',
    'jane@example.com',
    '$2b$12$WrntejsV/WPVXRfM0EFPy.X6nvy1UCwNTgPDCmayvYfhsVANRxGo.', 
    '1234567890',
    'female',
    '1995-04-20'
),
(
    'de227663-0fa8-4197-8495-e242368e209a',
    'Bob Smith', 
    'bob@unipetros.com', 
    '$2b$12$WrntejsV/WPVXRfM0EFPy.X6nvy1UCwNTgPDCmayvYfhsVANRxGo.', 
    '0987654321', 
    'male', 
    '1980-05-30'
);

DELETE FROM professors;

SELECT * FROM professors;

SELECT COUNT(id) AS count FROM professors

SELECT
    P.*,
    GROUP_CONCAT(S.id) AS subjects_ids,
    GROUP_CONCAT(S.name) AS subjects_names
FROM
    professors AS P
    LEFT JOIN professors_subjects AS PS ON PS.professor_id = P.id
    LEFT JOIN subjects AS S ON PS.subject_id = S.id
WHERE
    S.id IN (
        "3884079f-ec70-11ee-8ced-0242ac130002"
    )
GROUP BY
    P.id

 SELECT
    P.*,
    GROUP_CONCAT(S.id) AS subjects_ids,
    GROUP_CONCAT(S.name) AS subjects_names
FROM professors AS P
LEFT JOIN professors_subjects AS PS ON PS.professor_id = P.id
LEFT JOIN subjects AS S ON PS.subject_id = S.id
WHERE S.id IN ('38842e43-ec70-11ee-8ced-0242ac130002','388430e8-ec70-11ee-8ced-0242ac130002')
GROUP BY P.id

SELECT COUNT(*) as total_count FROM professors;