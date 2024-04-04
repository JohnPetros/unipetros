from typing import Dict, List
from datetime import date, timedelta

from entities.subject import Subject
from entities.professor import Professor

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

            students = students_repository.get_students()

            students_absents = students_repository.get_students_absents()

            students_dismissals = students_repository.get_students_dismissals()

            students_activity_by_range_days = {
                "7 days": self.__get_students_data_count_by_range_days(
                    range_days=7,
                    students=students,
                    students_dismissals=students_dismissals,
                    students_absents=students_absents,
                    total_students_count=total_students,
                ),
                "30 days": self.__get_students_data_count_by_range_days(
                    range_days=30,
                    students=students,
                    students_dismissals=students_dismissals,
                    students_absents=students_absents,
                    total_students_count=total_students,
                ),
                "90 days": self.__get_students_data_count_by_range_days(
                    range_days=90,
                    students=students,
                    students_dismissals=students_dismissals,
                    students_absents=students_absents,
                    total_students_count=total_students,
                ),
            }

            total_posts_by_category = posts_repository.get_posts_count_by_category()

            professors = professors_repository.get_professors()
            subjects = subjects_repository.get_subjects()

            professors_count_by_gender_and_subject = (
                self.__get_professors_count_by_gender_and_subject(professors, subjects)
            )

            popular_courses = courses_repository.get_courses_ordered_by_students_count()

            return {
                "total_professors": total_professors,
                "total_students": total_students,
                "total_subjects": total_subjects,
                "total_students_by_gender": total_students_by_gender,
                "total_posts_by_category": total_posts_by_category,
                "last_enrolled_students": last_enrolled_students,
                "popular_courses": popular_courses,
                "students_activity_by_range_days": students_activity_by_range_days,
                "professors_count_by_gender_and_subject": professors_count_by_gender_and_subject,
            }
        except Exception as exception:
            raise Error(error_message=exception) from exception

    def __get_professors_count_by_gender_and_subject(
        self, professors: List[Professor], subjects: List[Subject]
    ):
        subjects_ids = [subject.id for subject in subjects]

        male_professors = [
            professor for professor in professors if professor.gender == "male"
        ]

        female_professors = [
            professor for professor in professors if professor.gender == "female"
        ]

        data = []

        for index, subject_id in enumerate(subjects_ids):
            male_professors_count = 0
            female_professors_count = 0

            for male_professor in male_professors:
                professor_subjects_ids = [
                    subject.id for subject in male_professor.subjects
                ]

                if subject_id in professor_subjects_ids:
                    male_professors_count += 1

            for female_professor in female_professors:
                professor_subjects_ids = [
                    subject.id for subject in female_professor.subjects
                ]

                if subject_id in professor_subjects_ids:
                    female_professors_count += 1

            data.append(
                {
                    "subject_id": subject_id,
                    "subject_name": subjects[index].name,
                    "male_professors_count": male_professors_count,
                    "female_professors_count": female_professors_count,
                }
            )

        return data

    def __get_students_data_count_by_range_days(self, **kwargs) -> Dict:
        current_date = date.today()

        range_days = kwargs["range_days"]
        students = kwargs["students"]
        students_absents = kwargs["students_absents"]
        students_dismissals = kwargs["students_dismissals"]
        total_students_count = kwargs["total_students_count"]

        data = []

        for days in range(range_days, 0, -1):
            first_date = current_date - timedelta(days=days)
            enrollments_count = 0
            absents_count = 0
            dismissals_count = 0

            for student in students:
                if student.created_at == first_date:
                    enrollments_count += 1

            for absent in students_absents:
                if absent["date"] == first_date:
                    absents_count += 1

            for dismissal in students_dismissals:
                if dismissal["date"] == first_date:
                    dismissals_count += 1

            data.append(
                {
                    "date": first_date.strftime("%d/%m/%Y"),
                    "enrollments_count": enrollments_count,
                    "attendance": total_students_count - absents_count,
                    "dismissals_count": dismissals_count,
                }
            )

        return data
