# Есть два списка разной длины. В первом содержатся ключи, а во втором — значения.
# Напишите функцию make_dict, которая создаёт из этих ключей и значений словарь.
# Если ключу не хватило значения, в словаре должно быть значение None. Значения, которым
# не хватило ключей, нужно игнорировать. Обратите внимание! Функция должна возвращать
# созданный словарь. Приложите код решения.


def make_dict(keys, values) -> dict:
    dictionary = dict()
    for i in range(len(keys)):
        try:
            dictionary[keys[i]] = values[i]
        except IndexError:
            dictionary[keys[i]] = None
    return dictionary


print(make_dict(['apple', 'green', 'blue'], [5, 7, 4, 6, 8]))