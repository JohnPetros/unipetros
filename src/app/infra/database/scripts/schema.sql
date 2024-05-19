-- Active: 1716150162783@@127.0.0.1@3306@unipetros
CREATE DATABASE unipetros;

USE unipetros;

DROP TABLE IF EXISTS subjects;

CREATE TABLE IF NOT EXISTS subjects (
  id CHAR(36) DEFAULT (uuid()) PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE,
  description TEXT NOT NULL
);

INSERT INTO subjects (id, name, description) VALUES
(
  '3884079f-ec70-11ee-8ced-0242ac130002',
  'Design Digital', 
  'Este curso abrange os fundamentos do design digital, incluindo princípios de design, técnicas de criação de conteúdo visual, e ferramentas digitais para a criação de sites, gráficos, e mídias sociais. Os alunos aprenderão a aplicar estratégias de design para criar soluções digitais atraentes e eficazes.'
),
(
  '38842e43-ec70-11ee-8ced-0242ac130002',
  'Sistemas Operacionais', 
  'Este curso oferece uma introdução aos sistemas operacionais, explorando como eles gerenciam recursos de hardware e software, como processos, memória, e dispositivos de entrada/saída. Os alunos aprenderão sobre os principais sistemas operacionais, como Windows, Linux, e macOS, e como eles são usados em diferentes contextos, desde desktops até servidores.'
),
(
  '388430e8-ec70-11ee-8ced-0242ac130002',
  'Desenvolvimento Web', 
  'Este curso se concentra no desenvolvimento de aplicações web, ensinando os fundamentos de HTML, CSS, e JavaScript, além de frameworks e bibliotecas populares como React e Vue.js. Os alunos aprenderão a criar sites responsivos e dinâmicos, e a implementar funcionalidades web interativas.'
),
(
  '38843243-ec70-11ee-8ced-0242ac130002',
  'Engenharia de Software', 
  'Este curso aborda os princípios e práticas da engenharia de software, incluindo o ciclo de vida do desenvolvimento de software, gerenciamento de projetos, e metodologias ágeis. Os alunos aprenderão sobre a análise de requisitos, design de software, testes, e manutenção de sistemas de software.'
),
(
  '388432a9-ec70-11ee-8ced-0242ac130002',
  'Banco de dados',
   'Este curso cobre os conceitos fundamentais de bancos de dados, incluindo modelagem de dados, SQL, e sistemas de gerenciamento de banco de dados (DBMS). Os alunos aprenderão a projetar, implementar, e gerenciar bancos de dados para armazenar, recuperar, e manipular dados de forma eficiente.'
),
(
  '3884330b-ec70-11ee-8ced-0242ac130002',
  'Inglês', 
  'Este curso se concentra no desenvolvimento de habilidades de leitura, escrita, escuta, e fala em inglês. Os alunos aprenderão gramática, vocabulário, e expressões idiomáticas, além de técnicas de comunicação eficaz.'
),
(
  '38843484-ec70-11ee-8ced-0242ac130002',
  'Redes', 
  'Este curso aborda os fundamentos das redes de computadores, incluindo arquitetura de redes, protocolos de comunicação, e segurança de redes. Os alunos aprenderão sobre a configuração e gerenciamento de redes, e como proteger redes contra ameaças e ataques.'
),
(
  '38843533-ec70-11ee-8ced-0242ac130002',
  'Algoritmo', 
  'Este curso introduz os conceitos de algoritmos e estruturas de dados, que são fundamentais para a resolução de problemas de programação. Os alunos aprenderão a projetar e implementar algoritmos eficientes para resolver problemas complexos, além de entender como escolher e aplicar estruturas de dados apropriadas.'
);

DROP TABLE IF EXISTS courses;

CREATE TABLE IF NOT EXISTS courses (
  id CHAR(36) DEFAULT (uuid()) PRIMARY KEY,
  name VARCHAR(255),
  description TEXT
);

INSERT INTO courses (id, name, description)
VALUES 
(
  '01cbf711-ec80-11ee-8ced-0242ac130002',
  'Data Science Aplicada para Negócios',
   'Este curso se concentra em aplicar técnicas de Data Science para resolver problemas de negócios, utilizando ferramentas como Python, R e SQL. Os alunos aprendem a analisar grandes volumes de dados, criar modelos preditivos e visualizar insights de forma eficaz.'
),
(
  '01cd80a7-ec80-11ee-8ced-0242ac130002',
  'Inteligência Artificial e Machine Learning',
  'Este curso abrange os fundamentos da Inteligência Artificial e Machine Learning, ensinando como desenvolver algoritmos que podem aprender e melhorar com os dados. Os tópicos incluem redes neurais, aprendizado profundo e técnicas de otimização.'
),
(
  '01cdc72c-ec80-11ee-8ced-0242ac130002',
  'Desenvolvimento Web Moderno', 
  'Focado em tecnologias front-end e back-end, este curso ensina os desenvolvedores a criar aplicações web responsivas e interativas. Os alunos aprendem a usar frameworks populares como React, Angular e Vue.js, além de linguagens de back-end como Node.js e Python.'
),
(
  '01cdc995-ec80-11ee-8ced-0242ac130002',
  'Gestão de Projetos Ágeis', 
  'Este curso ensina as práticas e metodologias de gestão de projetos ágeis, como Scrum e Kanban, para melhorar a eficiência e a qualidade do desenvolvimento de software. Os alunos aprendem a planejar, executar e controlar projetos de forma iterativa e incremental.'
),
(
  '01cdc9fe-ec80-11ee-8ced-0242ac130002',
  'Segurança da Informação', 
  'Este curso aborda os princípios e práticas de segurança da informação, ensinando como proteger sistemas e dados contra ameaças. Os tópicos incluem criptografia, autenticação, segurança de rede e gestão de vulnerabilidades.'
),
(
  '01cdca5b-ec80-11ee-8ced-0242ac130002',
  'Análise e Desenvolvimento de Sistemas', 
  'O curso de Análise e Desenvolvimento de Sistemas é uma formação de tecnologia que prepara profissionais para implementar, desenvolver, manter e gerenciar sistemas computacionais, abrangendo desde a análise de necessidades até o design, codificação, testes e documentação de softwares. Este curso é voltado para a expansão do mercado de trabalho em Tecnologia da Informação (TI), com disciplinas que incluem Arquitetura de Computadores, Programação, Engenharia de Software, Banco de Dados, Gerenciamento de Projetos e Metodologias Ágeis, entre outras. A duração do curso é de aproximadamente 2 anos e meio, com mensalidades variando de acordo com a instituição de ensino e a modalidade de ensino escolhida'
);

DROP TABLE IF EXISTS courses_subjects;

CREATE TABLE IF NOT EXISTS courses_subjects (
  course_id CHAR(36) NOT NULL,
  subject_id CHAR(36) NOT NULL,
  PRIMARY KEY (course_id, subject_id),
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
  FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
);


INSERT INTO courses_subjects (course_id, subject_id) VALUES
('01cbf711-ec80-11ee-8ced-0242ac130002', '3884079f-ec70-11ee-8ced-0242ac130002'),
('01cd80a7-ec80-11ee-8ced-0242ac130002', '38842e43-ec70-11ee-8ced-0242ac130002'),
('01cdc72c-ec80-11ee-8ced-0242ac130002', '38843533-ec70-11ee-8ced-0242ac130002'),
('01cbf711-ec80-11ee-8ced-0242ac130002', '38843484-ec70-11ee-8ced-0242ac130002'),
('01cdca5b-ec80-11ee-8ced-0242ac130002', '38842e43-ec70-11ee-8ced-0242ac130002');

DROP TABLE IF EXISTS students;
CREATE TABLE IF NOT EXISTS students (
  id CHAR(36) DEFAULT (uuid()) PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL, 
  phone CHAR(11) NOT NULL, 
  avatar VARCHAR(255) DEFAULT 'default-avatar.png',
  birthdate DATE NOT NULL,
  gender ENUM('male', 'female'),
  created_at TIMESTAMP NOT NULL DEFAULT (UTC_TIMESTAMP),
  course_id CHAR(36) NOT NULL,
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
);

ALTER TABLE students ADD COLUMN is_active TINYINT NOT NULL DEFAULT 1;

INSERT INTO students (
  id, 
  name, 
  email, 
  password, 
  phone, 
  avatar,
  birthdate, 
  gender, 
  created_at,
  course_id,
  is_active
) 
VALUES
(
  '5b23d6aa-2f49-489a-be1d-427ef0b8d023',
  'Carlos Eduardo', 
  'carloseduardo@unipetros.com', 
  '$2b$12$rD0BBdCRlMr6xtlMgzw8K.KDtIcb0JmhA1IXwUkUZmqlpWqdWxOrO',
  '12987654321',
  'default-avatar.png',
  '1997-11-10',
  'male',
  '2024-05-18 23:34:20',
  '01cdc9fe-ec80-11ee-8ced-0242ac130002',
  '1'
),
(
  '9cf193f7-ec8e-488b-8d0e-3ed9fb144f77',
  'Maria Fernanda', 
  'mariafernanda@unipetros.com', 
  '$2b$12$CNGdUFM2GG86swcD1b6zUuBa554gdonBVjnGeL7JJy9l9lnnKH79.',
  '12987654321',
  'default-avatar.png',
  '1996-10-05',
  'female',
  '2024-03-29 23:34:20',
  '01cdc995-ec80-11ee-8ced-0242ac130002',
  '0'
),
(
  '9cf193f7-cc8e-488b-8d0e-3ed9fb144f77',
  'Jessie Kuhn', 
  'jessie@unipetros.com', 
  '$2b$12$CNGdUFM2GG86swcD1b6zUuBa554gdonBVjnGeL7JJy9l9lnnKH79.',
  '12987654321',
  'default-avatar.png',
  '1998-10-05',
  'male',
  '2024-05-09 23:34:20',
  '01cdc995-ec80-11ee-8ced-0242ac130002',
  '0'
),
(
  '7cf193f7-cc8e-488b-8d0e-3ed9fb144f77',
  'Katrina Ryan', 
  'katrina@unipetros.com', 
  '$2b$12$CNGdUFM2GG86swcD1b6zUuBa554gdonBVjnGeL7JJy9l9lnnKH79.',
  '12987654321',
  'default-avatar.png',
  '1997-10-05',
  'female',
  '2024-05-12 23:34:20',
  '01cdc995-ec80-11ee-8ced-0242ac130002',
  '1'
),
(
  '9cf193f7-ab8e-488b-8d0e-3ed9fb144f77',
  'Erika Matthews', 
  'erika@unipetros.com', 
  '$2b$12$CNGdUFM2GG86swcD1b6zUuBa554gdonBVjnGeL7JJy9l9lnnKH79.',
  '12987654321',
  'default-avatar.png',
  '1990-10-05',
  'female',
  '2024-05-05 23:34:20',
  '01cdc9fe-ec80-11ee-8ced-0242ac130002',
  '0'
),
(
  '9cf193f7-ad8e-488b-8d0e-3ed9fb144f77',
  'Kurt Bishop', 
  'kurt@unipetros.com', 
  '$2b$12$CNGdUFM2GG86swcD1b6zUuBa554gdonBVjnGeL7JJy9l9lnnKH79.',
  '12987654321',
  'default-avatar.png',
  '1991-10-05',
  'male',
  '2024-05-05 23:34:20',
  '01cdc995-ec80-11ee-8ced-0242ac130002',
  '1'
),
(
  '9cf193f7-ac8e-488b-8d0e-3ed9fb144f77',
  'Tara Soto', 
  'tara@unipetros.com', 
  '$2b$12$CNGdUFM2GG86swcD1b6zUuBa554gdonBVjnGeL7JJy9l9lnnKH79.',
  '12987654321',
  'default-avatar.png',
  '1995-10-05',
  'female',
  '2024-05-15 23:34:20',
  '01cd80a7-ec80-11ee-8ced-0242ac130002',
  '1'
),
(
  '9cf193f7-bc8e-488b-8d0e-3ed9fb144f77',
  'George Phillips', 
  'george@unipetros.com', 
  '$2b$12$CNGdUFM2GG86swcD1b6zUuBa554gdonBVjnGeL7JJy9l9lnnKH79.',
  '12987654321',
  'default-avatar.png',
  '1990-10-05',
  'male',
  '2024-05-05 23:34:20',
  '01cbf711-ec80-11ee-8ced-0242ac130002',
  '0'
),
(
  '9cf193f7-bc8e-488b-8d0f-3ed9fb144f77',
  'Dustin Brewer', 
  'dustin@unipetros.com', 
  '$2b$12$CNGdUFM2GG86swcD1b6zUuBa554gdonBVjnGeL7JJy9l9lnnKH79.',
  '12987654321',
  'default-avatar.png',
  '1995-10-05',
  'male',
  '2024-05-12 23:34:20',
  '01cd80a7-ec80-11ee-8ced-0242ac130002',
  '0'
),
(
  '9cf193f7-bc8e-488c-8d0e-3ed9fb144f77',
  'Lori Lopez', 
  'lori@unipetros.com', 
  '$2b$12$CNGdUFM2GG86swcD1b6zUuBa554gdonBVjnGeL7JJy9l9lnnKH79.',
  '12987654321',
  'default-avatar.png',
  '1999-10-05',
  'female',
  '2024-05-15 23:34:20',
  '01cdca5b-ec80-11ee-8ced-0242ac130002',
  '1'
),
(
  '9cf193f7-zc8e-488c-8d0e-3ed9fb144f77',
  'Carla Carpenter', 
  'carla@unipetros.com', 
  '$2b$12$CNGdUFM2GG86swcD1b6zUuBa554gdonBVjnGeL7JJy9l9lnnKH79.',
  '12987654321',
  'default-avatar.png',
  '2000-10-05',
  'female',
  '2024-05-10 23:34:20',
  '01cdc72c-ec80-11ee-8ced-0242ac130002',
  '1'
),
(
  '73e3c397-7c5c-406d-a45a-82642bd4b6cb',
  'Sofia Martins', 
  'sofiamartins@unipetros.com',
  '$2b$12$v/UILFnxM1nq6WCgDCWFNuO1hBDNrVS9wVM0DSDjYki8ozgIhjR0S',
  '12987654321',
  'default-avatar.png',
  '1998-12-15',
  'female',
  '2024-03-29 23:34:20',
  '01cdca5b-ec80-11ee-8ced-0242ac130002',
  '1'
),
(
  '39bee53f-4d2b-4f11-b861-28c3934a77f7',
  'Rafael Santos', 
  'rafaelsantos@unipetros.com',
  '$2b$12$lFnNvUIvZ7rzUAalD6LsPee9ekugEItfWjmzm0ftG5ALAYFpqjSuq',
  '12987654321',
  'default-avatar.png',
  '1999-01-20',
  'male',
  '2024-03-29 23:34:20',
  '01cbf711-ec80-11ee-8ced-0242ac130002',
  '1'
);

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

DROP TABLE IF EXISTS posts;

CREATE TABLE IF NOT EXISTS posts (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  content VARCHAR(255) NOT NULL,
  author_id CHAR(36) NOT NULL,
  category ENUM('academic', 'sport', 'study_tip'),
  FOREIGN KEY (author_id) REFERENCES students (id) ON DELETE CASCADE
);

INSERT INTO posts (id, title, content, author_id, category) VALUES
(
  'f899db78-ee05-11ee-9cc9-0242ac130002',
  'Dicas para o primeiro semestre', 
  'Algumas dicas úteis para os estudantes do primeiro semestre.', '5b23d6aa-2f49-489a-be1d-427ef0b8d023', 
  'study_tip'
),
(
  'f89e09c0-ee05-11ee-9cc9-0242ac130002',
  'Próxima partida de futebol', 
  'Informações sobre a próxima partida de futebol no campus.', '5b23d6aa-2f49-489a-be1d-427ef0b8d023', 
  'sport'
),
(
  'f89e4af3-ee05-11ee-9cc9-0242ac130002',
  'Como se preparar para exames', 
  'Dicas sobre como se preparar para exames, incluindo estratégias de estudo e técnicas de revisão.', 
  '5b23d6aa-2f49-489a-be1d-427ef0b8d023', 
  'study_tip'
),
(
  'f89e4e72-ee05-11ee-9cc9-0242ac130002',
  'Plano de estudos para o próximo semestre',
  'Um plano de estudos detalhado para ajudar os estudantes a se organizarem para o próximo semestre.', 
  '5b23d6aa-2f49-489a-be1d-427ef0b8d023',
  'study_tip'
),
(
  'f89e4fdb-ee05-11ee-9cc9-0242ac130002',
  'Treino de futebol para iniciantes', 
  'Um guia para iniciantes interessados em começar a jogar futebol no campus.', '5b23d6aa-2f49-489a-be1d-427ef0b8d023',
  'sport'
),
(
  'f89e50cf-ee05-11ee-9cc9-0242ac130002',
  'Dicas para o estudo de programação',
  'Algumas dicas para estudantes interessados em programação, incluindo recursos e estratégias', 
  '5b23d6aa-2f49-489a-be1d-427ef0b8d023', 
  'study_tip'
),
(
  'f89e51bb-ee05-11ee-9cc9-0242ac130002',
  'Como se preparar para a vida após a graduação', 
  'Um guia para ajudar os estudantes a se prepararem para a vida após a graduação, incluindo dicas de carreira e planejamento financeiro.', 
  '5b23d6aa-2f49-489a-be1d-427ef0b8d023',
  'academic'
),
(
  'f89e529c-ee05-11ee-9cc9-0242ac130002',
  'Próximos eventos culturais no campus', 
  'Informações sobre os próximos eventos culturais no campus, incluindo datas e locais.', '5b23d6aa-2f49-489a-be1d-427ef0b8d023', 
  'academic'
),
(
  'f89e5387-ee05-11ee-9cc9-0242ac130002',
  'Dicas para o estudo de matemática', 
  'Algumas dicas para estudantes que estão lutando com matemática, incluindo recursos e estratégias.', 
  '5b23d6aa-2f49-489a-be1d-427ef0b8d023',
  'study_tip'
),
(
  'f89e545e-ee05-11ee-9cc9-0242ac130002',
  'Como se manter saudável durante a pandemia', 
  'Dicas para manter-se saudável durante a pandemia, incluindo exercícios físicos e práticas de higiene.', 
  '5b23d6aa-2f49-489a-be1d-427ef0b8d023', 
  'study_tip'
);

DROP TABLE IF EXISTS professors;

CREATE TABLE IF NOT EXISTS professors (
    id CHAR(36) DEFAULT(uuid()) PRIMARY KEY, 
    name VARCHAR(255) NOT NULL, 
    email VARCHAR(255) NOT NULL UNIQUE, 
    password VARCHAR(255) NOT NULL, 
    phone VARCHAR(255) NOT NULL,
    birthdate DATE NOT NULL, 
    avatar VARCHAR(255) DEFAULT 'default-avatar.png', 
    gender ENUM('male', 'female')
);


INSERT INTO professors 
(id, name, email, password, phone, gender, birthdate)
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

DROP TABLE IF EXISTS professors_subjects;

CREATE TABLE IF NOT EXISTS professors_subjects (
  professor_id CHAR(36) NOT NULL,
  subject_id CHAR(36) NOT NULL,
  PRIMARY KEY (professor_id, subject_id),
  FOREIGN KEY (professor_id) REFERENCES professors(id) ON DELETE CASCADE,
  FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
);

INSERT INTO professors_subjects (professor_id, subject_id) VALUES
('062ac118-15de-46c8-974e-db33dfc46f38', '388432a9-ec70-11ee-8ced-0242ac130002'),
('d8e270de-509b-48dd-b485-5ec56cb2e55d', '388430e8-ec70-11ee-8ced-0242ac130002'),
('de227663-0fa8-4197-8495-e242368e209a', '38843533-ec70-11ee-8ced-0242ac130002');

DROP TABLE IF EXISTS admin;

CREATE TABLE IF NOT EXISTS admins (
  id CHAR(36) DEFAULT (uuid()) PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL, 
  avatar VARCHAR(255) DEFAULT 'default-avatar.png'
);

INSERT INTO admins (id, name, email, password) VALUES
(
  '5e557037-a936-11ee-b9aa-0242ac130002',
  'John Petros', 
  'john@unipetros.com',
  '$2b$12$WrntejsV/WPVXRfM0EFPy.X6nvy1UCwNTgPDCmayvYfhsVANRxGo.'
);
