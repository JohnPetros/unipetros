DROP TABLE IF EXISTS posts;

CREATE TABLE IF NOT EXISTS posts (
  id CHAR(36) DEFAULT (UUID()) PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  content VARCHAR(255) NOT NULL,
  author_id CHAR(36) NOT NULL,
  category ENUM('academic', 'sport', 'study_tip')
);

INSERT INTO posts (title, content, author_id, category) VALUES
('Dicas para o primeiro semestre', 'Algumas dicas úteis para os estudantes do primeiro semestre.', '5e557037-e936-11ee-b9aa-0242ac130002', 'study_tip'),
('Próxima partida de futebol', 'Informações sobre a próxima partida de futebol no campus.', '5e557037-e936-11ee-b9aa-0242ac130002', 'sport'),
('Como se preparar para exames', 'Dicas sobre como se preparar para exames, incluindo estratégias de estudo e técnicas de revisão.', '5e557037-e936-11ee-b9aa-0242ac130002', 'study_tip'),
('Plano de estudos para o próximo semestre', 'Um plano de estudos detalhado para ajudar os estudantes a se organizarem para o próximo semestre.', '5e557037-e936-11ee-b9aa-0242ac130002', 'study_tip'),
('Treino de futebol para iniciantes', 'Um guia para iniciantes interessados em começar a jogar futebol no campus.', '5e557037-e936-11ee-b9aa-0242ac130002', 'sport'),
('Dicas para o estudo de programação', 'Algumas dicas para estudantes interessados em programação, incluindo recursos e estratégias.', '5e557037-e936-11ee-b9aa-0242ac130002', 'study_tip'),
('Como se preparar para a vida após a graduação', 'Um guia para ajudar os estudantes a se prepararem para a vida após a graduação, incluindo dicas de carreira e planejamento financeiro.', '5e557037-e936-11ee-b9aa-0242ac130002', 'academic'),
('Próximos eventos culturais no campus', 'Informações sobre os próximos eventos culturais no campus, incluindo datas e locais.', '5e557037-e936-11ee-b9aa-0242ac130002', 'academic'),
('Dicas para o estudo de matemática', 'Algumas dicas para estudantes que estão lutando com matemática, incluindo recursos e estratégias.', '5e557037-e936-11ee-b9aa-0242ac130002', 'study_tip'),
('Como se manter saudável durante a pandemia', 'Dicas para manter-se saudável durante a pandemia, incluindo exercícios físicos e práticas de higiene.', '5e557037-e936-11ee-b9aa-0242ac130002', 'study_tip');

SELECT * FROM posts;

SELECT category, COUNT(category) AS count 
FROM posts 
GROUP BY category;