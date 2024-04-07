from .create_professors_by_csv import CreateProfessorsByCSV
from .create_professor import CreateProfessor
from .get_professors_page_data import GetProfessorsPageData
from .get_professor_details_page_data import GetProfessorDetailsPageData
from .get_subjects_page_data import GetSubjectsPageData
from .create_subject import CreateSubject
from .get_students_page_data import GetStudentsPageData
from .create_student import CreateStudent
from .create_students_by_csv import CreateStudentsByCSV
from .get_courses_page_data import GetCoursesPageData
from .create_course import CreateCourse
from .create_subjects_by_csv import CreateSubjectsByCSV
from .create_courses_by_csv import CreateCoursesByCSV
from .get_analytics_page_data import GetAnalyticsPageData

get_professor_details_page_data = GetProfessorDetailsPageData()
get_professors_page_data = GetProfessorsPageData()
create_professor = CreateProfessor()
create_professors_by_csv = CreateProfessorsByCSV()

get_subjects_page_data = GetSubjectsPageData()
create_subject = CreateSubject()
create_subjects_by_csv = CreateSubjectsByCSV()

get_students_page_data = GetStudentsPageData()
create_student = CreateStudent()
create_students_by_csv = CreateStudentsByCSV()

get_courses_page_data = GetCoursesPageData()
create_course = CreateCourse()
create_courses_by_csv = CreateCoursesByCSV()

get_analytics_page_data = GetAnalyticsPageData()
