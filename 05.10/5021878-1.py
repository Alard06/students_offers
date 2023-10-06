# Для расчета моды
import statistics

question = '00101010001-01-11-00'

count_resp = len(question)

print(f'Количество респондентов: {count_resp}')

# Создаем множество, тем самым уберем одинаковые
# символы в результатах (пер. question)
elements = set(question)
# Создаем словарь
count_el = {}
for item in elements:
    count_el[item] = question.count(item)

print(count_el)

# Имеющие муз. центр
prop_mus = count_el['1'] / count_resp * 100
# Не имеющие муз. центр
prop_n_mus = count_el['0'] / count_resp * 100
# Не ответили
prop_n_answer = count_el['-'] / count_resp * 100
# Сумма долей
sum = prop_n_answer + prop_n_mus + prop_mus

print(f'Доля респондентов, имеющие музыкальный центр: {prop_mus} %')
print(f'Доля респондентов, не имеющие музыкальный центр: {prop_n_mus} %')
print(f'Доля респондентов, не ответивших на вопрос: {prop_n_answer} %')
print(f'Сумма долей: {sum} %')
print(f'Мода ответов на вопрос (import statistics): {statistics.mode(question)}')

moda = 0
moda_el = 0
for item, count in count_el.items():
    if moda < count:
        moda = count
        moda_el = item

print(f'Мода ответов на вопрос (цикл for): {moda_el}')




