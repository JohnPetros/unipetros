USE unipetros;

DROP TABLE IF EXISTS subjects;

CREATE TABLE IF NOT EXISTS subjects (
  id CHAR(36) DEFAULT (uuid()) PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE,
  description TEXT NOT NULL
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