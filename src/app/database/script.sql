-- Active: 1711212961472@@127.0.0.1@3306@unipetros
CREATE DATABASE IF NOT EXISTS unipetros;

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
('John Petros', 'john@unipetros.com', '$2b$12$WrntejsV/WPVXRfM0EFPy.X6nvy1UCwNTgPDCmayvYfhsVANRxGo.')

SELECT * FROM admins

SELECT UTC_DATE() As Result;

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


SELECT * FROM professors

DELETE FROM professors

DROP TABLE IF EXISTS subjects;
CREATE TABLE IF NOT EXISTS subjects (
  id CHAR(36) DEFAULT (uuid()) PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE
);

ALTER TABLE subjects ADD COLUMN description VARCHAR(255);

ALTER TABLE subjects MODIFY COLUMN description TEXT;

INSERT INTO subjects (name, description) VALUES
('Design Digital', 'Este curso abrange os fundamentos do design digital, incluindo princípios de design, técnicas de criação de conteúdo visual, e ferramentas digitais para a criação de sites, gráficos, e mídias sociais. Os alunos aprenderão a aplicar estratégias de design para criar soluções digitais atraentes e eficazes.'),
('Sistemas Operacionais', 'Este curso oferece uma introdução aos sistemas operacionais, explorando como eles gerenciam recursos de hardware e software, como processos, memória, e dispositivos de entrada/saída. Os alunos aprenderão sobre os principais sistemas operacionais, como Windows, Linux, e macOS, e como eles são usados em diferentes contextos, desde desktops até servidores.'),
('Desenvolvimento Web', 'Este curso se concentra no desenvolvimento de aplicações web, ensinando os fundamentos de HTML, CSS, e JavaScript, além de frameworks e bibliotecas populares como React e Vue.js. Os alunos aprenderão a criar sites responsivos e dinâmicos, e a implementar funcionalidades web interativas.'),
('Engenharia de Software', 'Este curso aborda os princípios e práticas da engenharia de software, incluindo o ciclo de vida do desenvolvimento de software, gerenciamento de projetos, e metodologias ágeis. Os alunos aprenderão sobre a análise de requisitos, design de software, testes, e manutenção de sistemas de software.'),
('Banco de dados', 'Este curso cobre os conceitos fundamentais de bancos de dados, incluindo modelagem de dados, SQL, e sistemas de gerenciamento de banco de dados (DBMS). Os alunos aprenderão a projetar, implementar, e gerenciar bancos de dados para armazenar, recuperar, e manipular dados de forma eficiente.'),
('Inglês', ' Este curso se concentra no desenvolvimento de habilidades de leitura, escrita, escuta, e fala em inglês. Os alunos aprenderão gramática, vocabulário, e expressões idiomáticas, além de técnicas de comunicação eficaz.'),
('Redes', 'Este curso aborda os fundamentos das redes de computadores, incluindo arquitetura de redes, protocolos de comunicação, e segurança de redes. Os alunos aprenderão sobre a configuração e gerenciamento de redes, e como proteger redes contra ameaças e ataques.'),
('Algoritmo', 'Este curso introduz os conceitos de algoritmos e estruturas de dados, que são fundamentais para a resolução de problemas de programação. Os alunos aprenderão a projetar e implementar algoritmos eficientes para resolver problemas complexos, além de entender como escolher e aplicar estruturas de dados apropriadas.');

SELECT * FROM subjects

DELETE FROM subjects


DROP TABLE IF EXISTS professors_subjects;
CREATE TABLE IF NOT EXISTS professors_subjects (
  professor_id CHAR(36) NOT NULL,
  subject_id CHAR(36) NOT NULL,
  PRIMARY KEY (professor_id, subject_id),
  FOREIGN KEY (professor_id) REFERENCES professors(id) ON DELETE CASCADE,
  FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
);

INSERT INTO professors_subjects (professor_id, subject_id) VALUES
('b5e426b9-e93a-11ee-b9aa-0242ac130002', 'c86ba7d1-e93b-11ee-b9aa-0242ac130002'),
('b5e426b9-e93a-11ee-b9aa-0242ac130002', 'c86ba520-e93b-11ee-b9aa-0242ac130002'),
('b5e426b9-e93a-11ee-b9aa-0242ac130002', 'c86ba843-e93b-11ee-b9aa-0242ac130002'),
('ed0d310b-e93b-11ee-b9aa-0242ac130002', 'c86ba843-e93b-11ee-b9aa-0242ac130002'),
('ed0d6319-e93b-11ee-b9aa-0242ac130002', 'c86acfb0-e93b-11ee-b9aa-0242ac130002');

SELECT 
  P.*, 
  GROUP_CONCAT(S.id) AS subjects_ids, 
  GROUP_CONCAT(S.name) AS subjects_names
FROM professors AS P
LEFT JOIN professors_subjects AS PS ON PS.professor_id = P.id 
LEFT JOIN subjects AS S ON PS.subject_id = S.id
GROUP BY P.id
