from models import *


def main():

    mary = Position("Mary", 1, 250, 6, 1, 18)
    ann = Position("Ann", 1, 500, 8, 5, 20)
    bob = Position("Bob", 1, 100, 7, 3, 36)
    andry = Maker("Andry", 3, 459, 4, 4, 40, 10, 4)
    mark = Maker("Mark", 2, 550, 6, 5, 22, 8, 5)
    lala = Technical("Lala", 6, 120, 4, 1, 31, 7, 5, "Apple")
    katy = Performer("Katy", 5, 630, 5, 5, 38, 10, True)
    ivan = MainRole("Ivan", 5, 450, 8, 5, 19, 20, True, False, 3)

    list_of_employees = StudioManager([mary, ann, bob, andry, mark, lala, katy, ivan])

    print("\nEmployees needed to film historical films:")
    list_of_employees.search_by_film_type(FilmType.Historical)
    print("\nSort employees by salery:")
    list_of_employees.sort_by_salery(Sort.DESC)
    print("\nSort employees by working hours:")
    list_of_employees.sort_by_hours(Sort.ASC)


if __name__ == '__main__':
    main()
