def task_1():
    try:
        input_year = int(input('Введите дату рождения:\n>>> '))
        if input_year < 1900 or input_year > 2050:
            raise 'Год должен быть в диапазоне 1900-2050гг'
        return [x for x in range(input_year, input_year + 6)]
    except ValueError:
        print('Значение должно быть в формате XXXX')


def main():
    """Основная функция"""
    """  1. Создайте список years_list, содержащий год, 
    в который вы родились, и каждый последующий 
    год вплоть до вашего пятого дня рождения. 
    Например, если вы родились в 1980 году, 
    список будет выглядеть так: 
    years_list = [1980, 1981,1982, 1983, 1984, 1985]."""
    year_list = task_1()
    print(f'Список year_list: {year_list}')

    """ 2. В какой из годов, содержащихся в списке years_list, 
    был ваш третий день рождения? Помните, в первый год 
    вам было 0 лет."""
    print(f'Третий день рождения: {year_list[3]}')

    """3. В какой из годов, перечисленных в списке 
    years_list, вам было больше всего лет?"""
    print(f'Больше всего лет: {max(year_list)}')

    """4. Создайте список things, содержащий три элемента:
     "mozzarella", "cinderella", "salmonella"."""
    things = ["mozzarella", "cinderella", "salmonella"]

    """5. Напишите с большой буквы тот элемент списка 
    things, который относится к человеку, а затем 
    выведите список. Изменился ли элемент списка?"""
    things[1] = things[1].capitalize()
    print(things)

    """6. Переведите сырный элемент списка things в 
    верхний регистр целиком и выведите список."""
    things[0] = things[0].upper()
    print(things)

    """7. Удалите болезнь из списка things, получите 
    Нобелевскую премию и затем выведите список на экран."""
    things.remove("salmonella")
    things.append('Нобелевская премия')
    print(things)

    """8. Создайте список, который называется surprise и
     содержит элементы 'Groucho', 'Chico' и 'Harpo'."""
    surprise = ['Groucho', 'Chico', 'Harpo']

    """9. Напишите последний элемент списка surprise со 
    строчной буквы, затем обратите его и напишите с прописной буквы."""
    last_element = surprise[-1].lower()
    last_element_reversed = last_element[::-1]
    last_element_reversed_capitalized = last_element_reversed.capitalize()
    print(last_element_reversed_capitalized)

    """10. Создайте англо-французский словарь, 
    который называется e2f, и выведите его на экран. 
    Вот ваши первые слова: dog/chien, cat/chat и walrus/morse."""
    e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
    print(e2f)

    """11. Используя словарь e2f, выведите французский вариант слова walrus."""
    print(e2f['walrus'])

    """Создайте французско-английский словарь f2e на основе словаря e2f. Используйте метод items."""
    f2e = {french: english for english, french in e2f.items()}
    print(f2e)

    """13. Используя словарь f2e, выведите английский вариант слова chien."""
    print(f2e['chien'])

    """14. Создайте и выведите на экран множество английских слов из ключей словаря e2f."""
    english_words = set(e2f.keys())
    print(english_words)


    """15. Создайте многоуровневый словарь life. 
    Используйте следующие строки для ключей верхнего уровня: 
    'animals', 'plants' и 'other'.
    Сделайте так, чтобы ключ 'animals' ссылался на другой 
    словарь, имеющий ключи 'cats', 'octopi' и 'emus'.
    Сделайте так, чтобы ключ 'cats' ссылался на список 
    строк со значениями 'Henri', 'Grumpy' и 'Lucy'. 
    Остальные ключи должны ссылаться на пустые словари."""
    life = {
        'animals': {
            'cats': ['Henri', 'Grumpy', 'Lucy'],
            'octopi': {},
            'emus': {}
        },
        'plants': {},
        'other': {}
    }

    """16. Выведите на экран высокоуровневые ключи словаря life."""
    print(life.keys())

    """17. Выведите на экран ключи life['animals']."""
    print(life['animals'].keys())

    """18. Выведите значения life['animals']['cats']."""
    print(life['animals']['cats'])


if __name__ == '__main__':
    main()
