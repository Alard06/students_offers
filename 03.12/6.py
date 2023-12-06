def to_int(text):
    digits = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8,
              'девять': 9}
    tens = {'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать':
        15, 'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19}
    decades = {'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70,
               'восемьдесят': 80, 'девяносто': 90}
    hundreds = {'сто': 100, 'двести': 200, 'триста': 300, 'четыреста': 400, 'пятьсот': 500, 'шестьсот': 600,
                'семьсот': 700, 'восемьсот': 800, 'девятьсот': 900}

    words = text.split()
    result = 0
    prev = None
    for word in words:
        if word in digits:
            if prev and prev in tens:
                print(f'{word} - некорректное расположение в числе')
                return -1
            result += digits[word]
        elif word in tens:
            if prev and prev in tens:
                print(f'{word} - некорректное расположение в числе')
                return -1
            result += tens[word]
        elif word in decades:
            if prev and (prev in tens or prev in decades):
                print(f'{word} - некорректное расположение в числе')
                return -1
            result += decades[word]
        elif word in hundreds:
            if prev and prev != 'и':
                print(f'{word} - некорректное расположение в числе')
                return -1
            result += hundreds[word]
        elif word == 'тысяча':
            if prev and prev != 'и':
                print(f'{word} - некорректное расположение в числе')
                return -1
            result *= 1000
        elif word == 'и':
            pass
        else:
            print(f'{word} - некорректное расположение в числе')
            return -1
        prev = word

    return result

print(to_int('девять'))
print(to_int('десять'))
print(to_int('одиннадцать'))
print(to_int("сто сорок тридцать два сто"))
print(to_int("сто сорок сто два сто"))
print(to_int('тридцать три'))