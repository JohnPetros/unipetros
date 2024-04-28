from typing import List

from core.commons.email import Email
from core.entities.professor import Professor

from infra.repositories import professors_repository


class GetFilteredProfessors:
    def excute(
        self,
        name_or_email: str = "",
        subjects_ids: List = [],
        page_number: int = 1,
        gender: str = "all",
    ) -> tuple[list[Professor], int]:
        professors = []

        if not page_number:
            page_number = 1

        if name_or_email:
            email = Email(name_or_email)
            is_email = email.validate()

            if is_email:
                professors = professors_repository.get_filtered_professors(
                    email=email.value,
                    subjects_ids=subjects_ids,
                    page_number=page_number,
                    gender=gender,
                )
            else:
                professors = professors_repository.get_filtered_professors(
                    name=name_or_email,
                    subjects_ids=subjects_ids,
                    page_number=page_number,
                    gender=gender,
                )
        else:
            professors = professors_repository.get_filtered_professors(
                name=name_or_email,
                subjects_ids=subjects_ids,
                page_number=page_number,
                gender=gender,
            )

        professors_count = professors_repository.get_professors_count()

        return professors, professors_count
