# Напишите простой калькулятор. У вас должна быть функция calculate,
# которая принимает три аргумента: первые два — числа, третий — операция,
# которая должна быть произведена над ними. Доступные операции: сложение,
# вычитание, умножение и деление. Функция возвращает результат операции.
# В остальных случаях функция должна вернуть строку «Неизвестная операция»


def calculate(a, b, op) -> str:
    result = 0
    if op == '+':
        result = a + b
        return str(result)
    if op == '-':
        result = a - b
        return str(result)
    if op == '*':
        result = a * b
        return str(result)
    if op == '/':
        try:
            result = a / b
            return str(result)
        except ZeroDivisionError:
            return 'Произошло деление на 0'
    else:
        return 'Неизвестная операция'

print(calculate(1, 2, '//'))