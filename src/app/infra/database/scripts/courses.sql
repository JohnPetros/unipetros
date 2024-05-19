-- Active: 1715824547022@@127.0.0.1@3306@unipetros
DROP TABLE IF EXISTS courses;

CREATE TABLE IF NOT EXISTS courses (
  id CHAR(36) DEFAULT (uuid()) PRIMARY KEY,
  name VARCHAR(255),
  description TEXT
);

INSERT INTO courses (name, description)
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

SELECT * FROM courses;

SELECT 
  C.*, 
  GROUP_CONCAT(S.id) AS subjects_ids, 
  GROUP_CONCAT(S.name) AS subjects_names
FROM courses AS C
JOIN courses_subjects AS CS ON CS.course_id = C.id 
JOIN subjects AS S ON CS.subject_id = S.id
GROUP BY C.id;

SELECT C.*, COUNT(S.id) AS students_count
FROM courses AS C
LEFT JOIN students AS S ON S.course_id = C.id
GROUP BY C.id
LIMIT 4

DELETE FROM courses;
