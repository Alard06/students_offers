import statistics
import time

import numpy as np  # python pip install numpy


def main():
    PC = [18, 20, 23, 26, 29, 32, 35, 36, 39, 43, 44, 47, 49, 49, 50, 51, 51, 57, 61, 63]
    average = sum(PC)/len(PC)  # statistics.mean(PC)
    median = statistics.median(PC)
    moda = statistics.mode(PC)
    min_row = min(PC)
    max_row = max(PC)
    sum_row = sum(PC)
    count_obs = len(PC)
    std_d = statistics.stdev(PC)  # Отклонение
    std_er = np.std(PC)/np.sqrt(len(PC))
    variance = np.var(PC)  # Дисперсия
    range_of_data = max_row - min_row   # Размах ряда

    print(f"""Описательная статистика временного ряда:
Среднее арифметическое = {average}
Стандартная ошибка = {round(std_er, 2)}
Медиана = {median}
Мода = {moda}
Стандартное отклонение = {round(std_d, 2)}
Дисперсия = {variance}
Размах = {range_of_data}
Минимальное значение ряда = {min_row}
Максимальное значение ряда = {max_row}
Сумма = {sum_row}
Количество наблюдений = {count_obs}""")


if __name__ == '__main__':
    # main()
    for i in range(1000):
        time.sleep(2)
        print('\a')