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
('062ac118-15de-46c8-974e-db33dfc46f38', '5b23d6aa-2f49-489a-be1d-427ef0b8d023'),
('d8e270de-509b-48dd-b485-5ec56cb2e55d', '38843533-ec70-11ee-8ced-0242ac130002'),
('de227663-0fa8-4197-8495-e242368e209a', '38843484-ec70-11ee-8ced-0242ac130002');

SELECT 
  P.*, 
  GROUP_CONCAT(S.id) AS subjects_ids, 
  GROUP_CONCAT(S.name) AS subjects_names
FROM professors AS P
LEFT JOIN professors_subjects AS PS ON PS.professor_id = P.id 
LEFT JOIN subjects AS S ON PS.subject_id = S.id
GROUP BY P.id;

SELECT 
  COUNT(P.id) AS professors_count,
  P.gender, S.name
FROM professors AS P
LEFT JOIN professors_subjects AS PS ON PS.professor_id = P.id 
LEFT JOIN subjects AS S ON PS.subject_id = S.id
GROUP BY P.gender
GROUP BY S.name

DELETE FROM professors_subjects;