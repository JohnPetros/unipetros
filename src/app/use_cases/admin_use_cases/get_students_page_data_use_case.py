from repositories import students_repository, courses_repository

from forms.student_form import StudentForm

from utils.error import Error


class GetStudentsPageDataUseCase:
    def excute(self):
        try:
            students = students_repository.get_students()
            courses = courses_repository.get_courses()

            student_form = StudentForm()
            student_form.course.choices = [
                (course.id, course.name) for course in courses
            ]

            return {
                "students": students,
                "student_form": student_form,
            }

        except Exception as exception:
            return Error(exception, 500)
