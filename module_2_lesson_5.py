# Название программы и темы

print('Модуль 2, урок 5.')
print('Функции.')

# Запрос имени пользователя и приветствие

name = input('Здравствуйте, введите ваше имя: ')
print('Привет,', name)
print('Сегодня мы начнём работать с функциями.')
print('Создадим функцию с тремя параметрами n, m и value,')
print('которая будет создавать матрицу(вложенный список)')
print('размерами n строк и m столбцов, заполненную значениями value')


# определяем функцию заполняющую список
# задали значения по умолчанию, на случай если параметров не передали.
def get_matrix(n=1, m=1, value=0):
    # создаем пустой список
    matrix_list = []

    # последовательно создаём n вложенных пустых списков
    for i in range(n):
        matrix_list.append([])

        # во вложенный список записываем m значений value
        for j in range(m):
            matrix_list[i].append(value)

    # Возвращаем полученный результат
    return matrix_list


# передаём контрольные значения в функцию
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# печатаем полученные результаты
print('Первая матрица:', result1)
print('Вторая матрица:', result2)
print('Третья матрица:', result3)

# отдельно вызовем функцию без параметров
print('Матрица с параметрами по умолчанию:', get_matrix())

# Окончание программы
print('Работа программы закончена.')
print('Пока,', name + '!', 'Увидимся на следующих уроках!')






# обычные
# def say_hello():
#   print('Hello')

# say_hello()


# принимающие
# def say_hello(name):
#    print('Hello', name)


# say_hello('Nik')


# возвращающие

# import random


# def lottery():
#    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#    win = random.choice(tickets)
#    return win
#
# winner = lottery()
# print(winner)

# import random

# def lottery(mon, thue):
#    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#    win1 = random.choice(tickets)
#    tickets.remove(win1)
#    win2 = random.choice(tickets)
#    print(mon, thue)
#    return win1, win2


# winner1, winner2 = lottery('monday', 'thuesday')
# print(winner1, winner2)

# import random

# def lottery(*args, **kwargs):
#    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#    win1 = random.choice(tickets)
#    tickets.remove(win1)
#    win2 = random.choice(tickets)
#    print(*args)
#    return win1, win2


# winner1, winner2 = lottery('monday', 'thuesday', 'friday')
# print(winner1, winner2)

# использование значений по умолчанию
# def test(a=2,b=True):
#    print(a,b)

# test()
# test(8,12)
# test()
# test([1,2])
# test(*[1,2])


# анонимные
