def insert_underscore(s):
    s = '_'.join(s.split())
    return s

print('Результат: ', insert_underscore(input('Введите строку: ')))