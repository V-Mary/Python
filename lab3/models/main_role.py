from models.performer import Performer
from models.enums.sport import Sport


class MainRole(Performer):
    def __init__(self, name, job, salery, working_hours, film_type, age, number_of_performances, popylarity,
                 ability_to_sing: bool, sport_skills: Sport):
        super().__init__(name, job, salery, working_hours, film_type, age, number_of_performances, popylarity)
        self. ability_to_sing = ability_to_sing
        self.sport_skills = sport_skills
