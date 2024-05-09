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
('25edf049-f65d-11ee-b82f-0242ac140002', '64f2d2af-f65d-11ee-b82f-0242ac140002'),
('25edf40d-f65d-11ee-b82f-0242ac140002', '64f2d2af-f65d-11ee-b82f-0242ac140002'),
('25edf60d-f65d-11ee-b82f-0242ac140002', '64f2d498-f65d-11ee-b82f-0242ac140002');

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