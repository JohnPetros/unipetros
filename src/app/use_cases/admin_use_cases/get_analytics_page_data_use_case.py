from repositories import (
    professors_repository,
    students_repository,
    subjects_repository,
    courses_repository,
    posts_repository,
)

from utils.error import Error


class GetAnalyticsPageDataUseCase:
    def execute(self):
        try:
            total_professors = professors_repository.get_professors_count()
            total_students = students_repository.get_students_count()
            total_subjects = subjects_repository.get_subjects_count()

            total_students_by_gender = (
                students_repository.get_students_count_by_gender()
            )

            last_enrolled_students = students_repository.get_last_enrolled_students()

            total_posts_by_category = posts_repository.get_posts_count_by_category()

            popular_courses = courses_repository.get_courses_ordered_by_students_count()

            return {
                "total_professors": total_professors,
                "total_students": total_students,
                "total_subjects": total_subjects,
                "total_students_by_gender": total_students_by_gender,
                "total_posts_by_category": total_posts_by_category,
                "last_enrolled_students": last_enrolled_students,
                "popular_courses": popular_courses,
            }
        except Exception as exception:
            raise Error(error_message=exception) from exception
