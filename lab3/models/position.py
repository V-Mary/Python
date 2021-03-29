from models.enums.job import Job
from models.enums.film_type import FilmType


class Position:
    def __init__(self, name: str, job: Job, salery: int, working_hours: int, film_type: FilmType, age: int):
        self.name = name
        self.age = age
        self.job = job
        self.salery = salery
        self.working_hours = working_hours
        self.film_type = FilmType(film_type)
