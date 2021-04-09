from models.position import Position


class Performer(Position):

    def __init__(self, name, job, salery, working_hours, film_type, age, number_of_performances: int, popylarity: bool):
        super().__init__(name, job, salery, working_hours, film_type, age)
        self.number_of_performances = number_of_performances
        self.popylarity = popylarity
