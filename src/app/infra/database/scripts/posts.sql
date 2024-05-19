DROP TABLE IF EXISTS posts;

CREATE TABLE IF NOT EXISTS posts (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  content VARCHAR(255) NOT NULL,
  author_id CHAR(36) NOT NULL,
  category ENUM('academic', 'sport', 'study_tip'),
  FOREIGN KEY (author_id) REFERENCES students (id) ON DELETE CASCADE
);

INSERT INTO posts (title, content, author_id, category) VALUES
(
  'f899db78-ee05-11ee-9cc9-0242ac130002',
  'Dicas para o primeiro semestre', 
  'Algumas dicas úteis para os estudantes do primeiro semestre.', '5e557037-e936-11ee-b9aa-0242ac130002', 
  'study_tip'
),
(
  'f89e09c0-ee05-11ee-9cc9-0242ac130002',
  'Próxima partida de futebol', 
  'Informações sobre a próxima partida de futebol no campus.', '5e557037-e936-11ee-b9aa-0242ac130002', 
  'sport'
),
(
  'f89e4af3-ee05-11ee-9cc9-0242ac130002',
  'Como se preparar para exames', 
  'Dicas sobre como se preparar para exames, incluindo estratégias de estudo e técnicas de revisão.', 
  '5e557037-e936-11ee-b9aa-0242ac130002', 
  'study_tip'
),
(
  'f89e4e72-ee05-11ee-9cc9-0242ac130002',
  'Plano de estudos para o próximo semestre',
  'Um plano de estudos detalhado para ajudar os estudantes a se organizarem para o próximo semestre.', 
  '5e557037-e936-11ee-b9aa-0242ac130002',
  'study_tip'
),
(
  'f89e4fdb-ee05-11ee-9cc9-0242ac130002',
  'Treino de futebol para iniciantes', 
  'Um guia para iniciantes interessados em começar a jogar futebol no campus.', '5e557037-e936-11ee-b9aa-0242ac130002',
  'sport'
),
(
  'f89e50cf-ee05-11ee-9cc9-0242ac130002',
  'Dicas para o estudo de programação',
  'Algumas dicas para estudantes interessados em programação, incluindo recursos e estratégias', 
  '5e557037-e936-11ee-b9aa-0242ac130002', 
  'study_tip'
),
(
  'f89e51bb-ee05-11ee-9cc9-0242ac130002',
  'Como se preparar para a vida após a graduação', 
  'Um guia para ajudar os estudantes a se prepararem para a vida após a graduação, incluindo dicas de carreira e planejamento financeiro.', 
  '5e557037-e936-11ee-b9aa-0242ac130002',
  'academic'
),
(
  'f89e529c-ee05-11ee-9cc9-0242ac130002',
  'Próximos eventos culturais no campus', 
  'Informações sobre os próximos eventos culturais no campus, incluindo datas e locais.', '5e557037-e936-11ee-b9aa-0242ac130002', 
  'academic'
),
(
  'f89e5387-ee05-11ee-9cc9-0242ac130002',
  'Dicas para o estudo de matemática', 
  'Algumas dicas para estudantes que estão lutando com matemática, incluindo recursos e estratégias.', 
  '5e557037-e936-11ee-b9aa-0242ac130002', 7
  'study_tip'
),
(
  'f89e545e-ee05-11ee-9cc9-0242ac130002',
  'Como se manter saudável durante a pandemia', 
  'Dicas para manter-se saudável durante a pandemia, incluindo exercícios físicos e práticas de higiene.', 
  '5e557037-e936-11ee-b9aa-0242ac130002', 
  'study_tip'
);

SELECT * FROM posts;

SELECT category, COUNT(category) AS count 
FROM posts 
GROUP BY category;

DELETE FROM posts;
