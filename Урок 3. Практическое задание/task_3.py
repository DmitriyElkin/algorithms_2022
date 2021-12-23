"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

import hashlib


def num_substr(line):
    var_set = set()
    n = len(line)
    for i in range(n):
        for ii in range(i+1, n+1):
            substr = line[i:ii]
            if substr != line:
                var_set.add(hashlib.md5(substr.encode('utf-8')).hexdigest())
                # print(substr)

    print(f'{line} - {len(var_set)} уникальных подстрок')


num_substr('papa')
