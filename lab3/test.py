import unittest
from models import *


class TestStudioManager(unittest.TestCase):
    def setUp(self):
        self.mary = Position("Mary", 1, 250, 6, 1, 18)
        self.ann = Position("Ann", 1, 500, 8, 5, 20)
        self.bob = Position("Bob", 1, 100, 7, 3, 36)
        self.andry = Maker("Andry", 3, 459, 4, 4, 40, 10, 4)
        self.mark = Maker("Mark", 2, 550, 6, 5, 22, 8, 5)
        self.lala = Technical("Lala", 6, 120, 4, 1, 31, 7, 5, "Apple")
        self.katy = Performer("Katy", 5, 630, 5, 5, 38, 10, True)
        self.ivan = MainRole("Ivan", 5, 450, 8, 5, 19, 20, True, False, 3)
        self.list_of_employees =StudioManager([self.mary,  self.ann, self.bob, self.andry, self.mark, self.lala,
                                               self.katy, self.ivan])

    def test_search_by_film_type(self):
        self.assertEqual(self.list_of_employees.search_by_film_type(FilmType.Historical), [self.ann, self.mark,
                                                                                           self.katy, self.ivan])

    def test_sort_by_salery(self):
        # test sorting list with DESC argument
        self.assertEqual(self.list_of_employees.sort_by_salery(Sort.DESC), [self.katy, self.mark, self.ann, self.andry,
                                                                            self.ivan, self.mary,self.lala, self.bob])
        # test sorting list with ASC argument
        self.assertEqual(self.list_of_employees.sort_by_salery(Sort.ASC), [self.bob, self.lala, self.mary,self.ivan,
                                                                           self.andry, self.ann,self.mark, self.katy])

    def test_sort_by_hours(self):
        # test sorting list with DESC argument
        self.assertEqual(self.list_of_employees.sort_by_hours(Sort.DESC), [self.ann, self.ivan, self.bob, self.mary,
                                                                          self.mark, self.katy, self.andry, self.lala])
        # test sorting list with ASC argument
        self.assertEqual(self.list_of_employees.sort_by_hours(Sort.ASC), [self.andry, self.lala, self.katy, self.mary,
                                                                          self.mark, self.bob, self.ann, self.ivan])


if __name__ == "__main__":
  unittest.main()