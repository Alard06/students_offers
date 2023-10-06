age = int(input('Возраст: '))
gender = str(input('Введите Ваш пол: мужской - м, женский - ж: '))
if age < 0 or gender not in 'мж':
    print('Возраст не может быть отрицательным или такого пола не существует')
else:
    if 16 <= age <= 61 and gender == 'м':
        print(f'{age}: {gender} - трудоспособен')
    elif 16 <= age <= 56 and gender == 'ж':
        print(f'{age}: {gender} - трудоспособен')
    else:
        print(f'{age}: {gender} - НЕ трудоспособен')
