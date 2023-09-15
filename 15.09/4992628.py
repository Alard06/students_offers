# Известно количество студентов в каждой из шести групп каждого
# курса института (рис. 9.12( в файлах)). Организовать ввод информации
# по этой таблице и определить: а) на каком курсе обучается меньше всего
# студентов; б) какая из групп (указать ее номер и номер курса) самая ма- лочисленная;
# в) номер самой малочисленной группы (для каждого курса).
# PS Без доп. библиотек / простую программу


def tasks(data):
    min_sum = sum(data[0])
    min_sum_index = 0
    for i in range(len(data)):
        temp = sum(data[i])
        if min_sum > temp:
            min_sum_index = i

    print(f'а) меньше всего студентов обучается на: {min_sum_index + 1} курсе')

    print('б) какая из групп (указать ее номер и номер курса) самая ма- лочисленная;')

    min_numbers, min_course, min_group = 99, 0, 0
    for i in range(len(data)):
        temp = data[i].index(min(data[i]))
        if min_numbers > data[i][temp]:
            min_numbers = data[i][temp]
            min_group = temp
            min_course = i

    print(f'Курс: {min_course + 1} Группа: {min_group + 1} Количество: {data[min_course][min_numbers]}')

    # задание в
    print('в) номер самой малочисленной группы (для каждого курса).')
    for i in range(len(data)):
        print(f'Курс {i+1} Группа: {data[i].index(min(data[i])) + 1}')


def main():
    data = [
            [10, 24, 9, 8, 13, 4],
            [4, 13, 32, 17, 12, 10],
            [3, 1, 30, 19, 11, 4],
            [6, 9, 10, 12, 12, 10],
            [5, 4, 9, 23, 51, 7],
        ]
    op = int(input('Заполнить таблицу своими данными - 1; \nГотовыми - 2\n'))
    if op == 2:
        tasks(data)

    if op == 1:
        for i in range(5):
            for j in range(6):
                data[i][j] = int(input(f'Курс: {i+1}, группа {j+1}'))

        tasks(data)

main()
