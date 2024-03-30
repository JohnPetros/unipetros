from typing import Dict
from datetime import date, timedelta

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

            students_absents = students_repository.get_students_absents()

            students_absents_count_by_range_days = {
                "7 days": self.__get_students_absents_count_by_range_days(
                    7, students_absents, total_students
                ),
                "30 days": self.__get_students_absents_count_by_range_days(
                    30, students_absents, total_students
                ),
                "90 days": self.__get_students_absents_count_by_range_days(
                    90, students_absents, total_students
                ),
            }

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
                "students_absents_count_by_range_days": students_absents_count_by_range_days,
            }
        except Exception as exception:
            raise Error(error_message=exception) from exception

    def __get_students_absents_count_by_range_days(
        self, range_days: int, students_absents: Dict, total_students_count: int
    ) -> Dict:
        current_date = date.today()

        absents_count_by_date = []

        for days in range(range_days, -1, -1):
            first_date = current_date - timedelta(days=days)

            count = 0
            for absent in students_absents:
                if absent["date"] == first_date:
                    count += 1

            absents_count_by_date.append(
                {
                    "date": first_date.strftime("%d/%m/%Y"),
                    "absents_count": total_students_count - count,
                }
            )

        return absents_count_by_date
