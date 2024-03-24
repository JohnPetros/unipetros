from repositories.professors_repository import ProfessorsRepository

professors_repository = ProfessorsRepository()


class AdminController:
    def get_professors(self):
        professors = professors_repository.get_professors()

        print(professors[0].__dict__)

        return professors
