from .create_professors_by_csv_use_case import CreateProfessorsByCSVUseCase
from .create_professor_use_case import CreateProfessorUseCase
from .get_professors_page_data_use_case import GetProfessorsPageDataUseCase
from .get_professor_details_page_data_use_case import GetProfessorDetailsPageDataUseCase
from .get_subjects_page_data_use_case import GetSubjectsPageDataUseCase
from .create_subject_controller_use_case import CreateSubjectUseCase

get_professor_details_page_data_use_case = GetProfessorDetailsPageDataUseCase()
get_professors_page_data_use_case = GetProfessorsPageDataUseCase()
create_professor_use_case = CreateProfessorUseCase()
create_professors_by_csv_use_case = CreateProfessorsByCSVUseCase()

get_subjects_page_data_use_case = GetSubjectsPageDataUseCase()
create_subject_use_case = CreateSubjectUseCase()
