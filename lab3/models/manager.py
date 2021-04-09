from models.enums.film_type import FilmType
from models.enums.sort import Sort
from operator import attrgetter


class StudioManager:
    def __init__(self, employees: []):
        self.employees = employees

    def search_by_film_type(self, film_type: FilmType):
        new_list = list()
        for item in self.employees:
            if item.film_type == film_type:
                new_list.append(item)
                print(item.name)
        return new_list

    def sort_by_salery(self, sort: Sort):
        if sort == Sort.ASC:
            new_list = sorted(self.employees, key=attrgetter('salery'))
            for item in range(len(new_list)):
                print(new_list[item].name, "-", new_list[item].salery, "$")
            return new_list
        if sort == Sort.DESC:
            new_list = sorted(self.employees, key=attrgetter('salery'),  reverse=True)
            for item in range(len(new_list)):
                print(new_list[item].name, "-", new_list[item].salery, "$")
            return new_list

    def sort_by_hours(self, sort: Sort):
        if sort == Sort.ASC:
            new_list = sorted(self.employees, key=lambda x: x.working_hours)
            for item in range(len(new_list)):
                print(new_list[item].name, "-", new_list[item].working_hours, "hours")
            return new_list
        if sort == Sort.DESC:
            new_list = sorted(self.employees, key=attrgetter('working_hours'), reverse=True)
            for item in range(len(new_list)):
                print(new_list[item].name, "-", new_list[item].working_hours, "hours")
            return new_list
