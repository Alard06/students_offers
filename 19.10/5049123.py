def search_word(word, lst) -> bool:
    if word in lst:
        return True
    else:
        return False


def main():
    # SP = [2, 3, 'Экономика', 5, 2, True, 5, 10, 15, 'Hello']
    SP = [2, 3, 'Экономика', 2, True, 5, 10, 15, 'Hello']

    if search_word('Экономика', SP):
        print(f'Слово "Экономика" содержится в списке: {SP} \n {"-" * 10}')
        index_word = SP.index('Экономика')
        SP.pop(index_word)
        print(f'Удалено слово "Экономика". Вывод получившегося списка: \n{SP}\n {"-" * 10}')

    if search_word('Hallo', SP):
        print(f'Слово "Hallo" содержится в списке: {SP} \n {"-" * 10}')
    else:
        print(f'Слово "Hallo" НЕ содержится в списке: {SP} \n {"-" * 10}')
        new_string = "".join(chr(ord(letter) + 1) for letter in "Hallo")
        SP.append(new_string)
        print(f'Добавлено новое слово "{new_string}" в список: {SP} \n {"-" * 10}')

    if SP.count(5) == 1:
        SP.reverse()
        print(f'Цифра 5 встречается в списке 1 раз. Перевернутый список: \n{SP}')
    else:
        print(f'Цифра 5 встречается в списке {SP.count(5)} раз(а). Список очищен. ', end='')
        SP.clear()
        print(f'Вывод удаленного списка: \n{SP.clear()}')


if __name__ == "__main__":
    main()
