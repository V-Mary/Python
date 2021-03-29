from models.maker import Maker


class Technical(Maker):
    def __init__(self, name, job, salery, working_hours, film_type, age, number_of_fimls, films_rating, equipment: str):
        super().__init__(name, job, salery, working_hours, film_type, age, number_of_fimls, films_rating)
        self.equipment = equipment
