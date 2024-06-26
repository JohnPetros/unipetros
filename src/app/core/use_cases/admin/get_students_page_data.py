from infra.repositories import courses_repository
from infra.forms.student_form import StudentForm
from infra.utils.error import Error


class GetStudentsPageData:
    def excute(self):
        try:
            courses = courses_repository.get_courses()

            student_form = StudentForm()
            student_form.course.choices = [
                (course.id, course.name) for course in courses
            ]

            return {
                "student_form": student_form,
            }

        except Exception as exception:
            return Error(exception, 500)
