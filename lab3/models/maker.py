from models.position import Position


class Maker(Position):

    def __init__(self, name, job, salery, working_hours, film_type, age, number_of_fimls: int, films_rating: int):
        super().__init__(name, job, salery, working_hours, film_type, age)
        self.number_of_fimls = number_of_fimls
        self.films_rating = films_rating
