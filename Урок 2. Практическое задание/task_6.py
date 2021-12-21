"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""

from random import randint


def game(num=None, i=10):
    if num is None:
        num = randint(0, 100)
        print('Загадано число от 0 до 100')
    print(f'\nОсталось попыток: {i}')
    answer = int(input('Ваше число: '))
    if num == answer:
        print('\nВы угадали')
    elif i == 1:
        print(f'\nВы проиграли\nЗагаданное число: {num}')
    else:
        if answer < 0 or answer > 100:
            print('Ваше число вне диапазона')
        elif answer > num:
            print('Ваше число больше загаданного')
        elif answer < num:
            print('Ваше число меньше загаданного')
        game(num, i - 1)


game()
