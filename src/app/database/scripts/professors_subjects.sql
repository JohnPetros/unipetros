USE unipetros;

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