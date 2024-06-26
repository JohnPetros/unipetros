from .admins_repository import AdminsRepository
from .professors_repository import ProfessorsRepository
from .students_repository import StudentsRepository
from .subjects_repository import SubjectsRepository
from .courses_repository import CoursesRepository
from .posts_repository import PostsRepository

admins_repository = AdminsRepository()
professors_repository = ProfessorsRepository()
students_repository = StudentsRepository()
subjects_repository = SubjectsRepository()
courses_repository = CoursesRepository()
posts_repository = PostsRepository()
