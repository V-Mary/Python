"""
Порахувати кількість GET запитів (та вивести їх), що мали повернути зображення (містять слово images в назві запиту),
 які завершились успішно (код - 200), та були ініційовані машинами 72.30.79.46 та 90.7.158.134
 http://igm.univ-mlv.fr/~cherrier/download/L1/access.log
"""
import re


def main():
    input_file = "/Users/Mariya/Desktop/1_курс/Python/lab5/log_file.txt"

    regex_1 = r'72.30.79.46 - - \[(\d{2}\/\D{3}\/\d{4}):(\d{2}:\d{2}:\d{2}) ' \
              r'\+(0100|2000)] "GET /images/(.+)" 200 (.+)'

    with open(input_file, 'r') as file:
        counter = 0
        for line in file.readlines():
            found_1 = re.match(regex_1, line)
            if found_1 or found_2:
                print(found_1)
                counter += 1
    print(f'The number of successful GET: {counter}')


if __name__ == '__main__':
    main()
