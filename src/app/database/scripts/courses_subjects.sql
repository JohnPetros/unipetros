USE unipetros;

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

SELECT 
    C.*, 
    GROUP_CONCAT(S.id) AS subjects_ids, 
    GROUP_CONCAT(S.name) AS subjects_names
FROM courses AS C
JOIN courses_subjects AS CS ON CS.course_id = C.id 
JOIN subjects AS S ON CS.subject_id = S.id
GROUP BY C.id