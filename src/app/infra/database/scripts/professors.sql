-- Active: 1714258009743@@127.0.0.1@3306@unipetros
USE unipetros;

DROP TABLE IF EXISTS professors;

CREATE TABLE IF NOT EXISTS professors (
    id CHAR(36) DEFAULT(uuid()) PRIMARY KEY, name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL UNIQUE, password VARCHAR(255) NOT NULL, phone VARCHAR(255) NOT NULL, birthdate DATE NOT NULL, avatar VARCHAR(255) DEFAULT 'default-avatar.png', gender ENUM('male', 'female')
);

INSERT INTO
    professors (
        name, email, password, phone, gender, birthdate
    )
VALUES (
        'John Petros', 'john@unipetros.com', '$2b$12$WrntejsV/WPVXRfM0EFPy.X6nvy1UCwNTgPDCmayvYfhsVANRxGo.', '12123451234', 'male', '2002-03-16'
    ),
    (
        'Jane Doe', 'jane@example.com', '$2b$12$WrntejsV/WPVXRfM0EFPy.X6nvy1UCwNTgPDCmayvYfhsVANRxGo.', '1234567890', 'female', '1995-04-20'
    ),
    (
        'Bob Smith', 'bob@smith.com', '$2b$12$WrntejsV/WPVXRfM0EFPy.X6nvy1UCwNTgPDCmayvYfhsVANRxGo.', '0987654321', 'male', '1980-05-30'
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
    P.name LIKE '%joaoffgghh%'
    AND S.id IN (
        "388432a9-ec70-11ee-8ced-0242ac130002"
    )
GROUP BY
    P.id

SELECT * FROM a_table GROUP BY "08-08-2002";

SELECT COUNT(*) as total_count FROM professors;