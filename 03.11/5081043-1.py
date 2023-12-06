import random


def game(mode_game, number):
    iterable = -1
    if mode_game:
        while True:
            iterable = int(input("Введите число итераций: "))
            if iterable > 0:
                break
    else:
        iterable = ""

    while True:
        try:
            p_iterable = input("Выводить число, которое показывает во сколько раз больше/меньше вводимое число?\n "
                               "0 - не выводить \t 1 - выводить :")
            print(" ")
            if 0 == int(p_iterable) or int(p_iterable) == 1:
                break
            else:
                print("Введите число 1 или 0")
        except ValueError:
            print("Число должно быть целочисленным!")

    i = 0
    while iterable != "exit" or iterable == 0:
        input_number = input(f"Попытка {i + 1}. Введите число: ")
        if type(input_number) == float:
            input_number = int(input_number)

        if input_number == "exit":
            return 0

        if int(input_number) == number:
            print("Вы выиграли!")
            return 0
        elif int(input_number) > number:
            if int(p_iterable) == 1:
                print(f"Ваше число больше случайного на {round((int(input_number) / int(number)), 2)}")
            else:
                print(f"Ваше число больше случайного")
            i += 1
        elif int(input_number) < number:
            if int(p_iterable) == 1:
                print(f"Ваше число меньше случайного на {round((int(input_number) / int(number)), 2)}")
            else:
                print(f"Ваше число меньше случайного")
            i += 1
        else:
            print("Вы ввели не число")
        if i == iterable:
            print("Исчерпано количество попыток")
            return 0


def mode():
    while True:
        try:
            mode_g = int(input("Выберите режим отгадывания.\n0-пока не надоест\n1-За фиксированное число итераций\n>>> "))
            if mode_g in [0, 1]:
                break
        except ValueError:
            print("Вы ввели не целочисленное число!")

    if mode_g == 0:
        return False
    elif mode_g == 1:
        return True


def main():
    number = random.randrange(0, 101)
    game(mode_game=mode(), number=number)


if __name__ == '__main__':
    main()
