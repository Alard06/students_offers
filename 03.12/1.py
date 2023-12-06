import random


def full_name(fio: str):
    if fio.strip() == '' or len(fio.strip()) < 3:
        return 'Пустая строка или малая длина символов'
    name_list = fio.split()
    first_letters = f"{name_list[1][0]}.{name_list[2][0]}."

    # формируем строки в нужном формате
    result1 = f"{name_list[0]} {first_letters}"
    result2 = f"{first_letters} {name_list[0]}"

    # выводим результаты
    return [result1, result2]


print(full_name('  '))


def math_operations(expression: str):
    # Разбиваем выражение на числа и знаки операций
    tokens = []
    current_token = ""
    for char in expression:
        if char.isdigit():
            current_token += char
        else:
            if current_token != "":
                tokens.append(int(current_token))
                current_token = ""
            tokens.append(char)
    if current_token != "":
        tokens.append(int(current_token))

    # Инициализируем переменную для хранения текущего значения
    result = tokens[0]

    # Проходим по списку и выполняем операции
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        operand = tokens[i + 1]
        if operator == "+":
            result += operand
        elif operator == "-":
            result -= operand

    return result


# print(math_operations("5+5-10+10-4-10"))

def editing(string: str):
    split_string = string.strip().split()
    string = ' '.join(split_string)
    string_reverse = ' '.join([split_string[0].swapcase(), split_string[1].swapcase()] + split_string[2:])
    len_string = len(split_string)
    return [string, string_reverse, len_string]


print(editing("  test TEst teST "))


def test_editing():
    assert editing("  test TEst teST ") == ['test TEst teST', 'TEST teST teST', 3]
    assert editing("  aA e ba ") == ["aA e ba", "Aa E ba", 3]
    assert editing("  AB RA ca dabra ") == ["AB RA ca dabra", "ab ra ca dabra", 4]
    assert editing("word WoRdS  ") == ["word WoRdS", "WORD wOrDs", 2]
    print("OK")


test_editing()


def test():
    # просим пользователя ввести строку с названиями товаров
    products = "яблоки, груша, яблоки, киви, сливы, киви, киви, груша, груша, киви"

    # создаем словарь для подсчета количества каждого товара
    counts = {}

    # разбиваем строку на список товаров
    product_list = products.split(", ")

    # считаем количество каждого товара
    for product in product_list:
        if product in counts:
            counts[product] += 1
        else:
            counts[product] = 1

    # создаем список кортежей из пар "название товара - количество"
    product_counts = [(k, v) for k, v in counts.items()]

    # сортируем список по убыванию количества товара
    product_counts.sort(key=lambda x: x[1], reverse=True)

    # выводим таблицу
    print("Товар\tКоличество")
    for product, count in product_counts:
        print(f"{product}\t{count}")
    return product_counts


def symmetrical_difference(list_1=None, list_2=None):
    if None in [list_1, list_2]:
        list_1 = random.sample(range(1, 11), 5)
        list_2 = random.sample(range(1, 11), 5)
    set1 = set(list_1)
    set2 = set(list_2)

    sym_diff = set1.symmetric_difference(set2)
    return sym_diff


print(symmetrical_difference())

def symmetrical_difference(list_1=None, list_2=None):
    if None in [list_1, list_2]:
        list_1 = random.sample(range(1, 11), 5)
        list_2 = random.sample(range(1, 11), 5)
    set1 = set(list_1)
    set2 = set(list_2)

    sum_diff = set1.symmetric_difference(set2)
    return sum_diff

print(symmetrical_difference([4,5,6,7], [3,4,5,6,7]))




def number_to_words(num: int):
    ones = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    tens = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
            'девяносто']
    teens = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
             'семнадцать', 'восемнадцать', 'девятнадцать']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']

    if num == 0:
        return "ноль"

    if num < 0 or num > 1000:
        return "Ошибка: число должно быть от 0 до 1000"

    if num < 10:
        return ones[num]

    if num < 20:
        return teens[num % 10]

    if num < 100:
        return tens[num // 10] + (" " + ones[num % 10] if num % 10 != 0 else "")

    if num < 1000:
        return hundreds[num // 100] + (" " + number_to_words(num % 100) if num % 100 != 0 else "")

    if num == 1000:
        return "тысяча"


print(number_to_words(950))




def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a // b

ops_dict = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# op = input('Введите символ операции (+, -, *, /): ')
#
# if op in ops_dict:
#     result = ops_dict[op](a, b)
#     print(f'Результат: {result}')
# else:
#     print('Ошибка: некорректный символ операции')

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

import math

def reduce_fraction_1(n, m):
    gcd = math.gcd(n, m)
    p = n // gcd
    q = m // gcd
    return (p, q)


def reduce_fraction_2(fraction):
    n, m = fraction
    gcd = math.gcd(n, m)
    p = n // gcd
    q = m // gcd
    fraction[0] = p
    fraction[1] = q
    return [p, q]


def test_reduce_fraction_1():
  assert reduce_fraction_1(5, 10) == (1, 2)
  assert reduce_fraction_1(5, 5) == (1, 1)
  assert reduce_fraction_1(5, 15) == (1, 3)
  print('reduce_fraction_1 OK')

def test_reduce_fraction_2():
  assert reduce_fraction_2([5, 10]) == [1, 2]
  assert reduce_fraction_2([5, 5]) == [1, 1]
  assert reduce_fraction_2([5, 15]) == [1, 3]
  print(' reduce_fraction_2 OK')

test_reduce_fraction_1()
test_reduce_fraction_2()