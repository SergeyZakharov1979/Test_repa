from random import randint

print(f'''{'*' * 48}

    Приветствую вас в игре ЧИСЛОВАЯ УГАДАЙКА
        
    Предлагаю вам угадать число от 1 до 100

    ''')
print('*' * 48)
print()


def gen_random_num():
    return randint(1, 100)


def is_valid(n):
    if n.isdigit() and 1 <= int(n) <= 100:
        return True
    else:
        return False


def input_num():
    while True:
        n = input('Введите загаданное число?: ')
        if is_valid(n):
            return int(n)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')


def compare_num():
    hidden_num = gen_random_num()
    count = 0
    while True:
        n = input_num()
        count += 1
        if n > hidden_num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif n < hidden_num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        else:
            print(f'Вы угадали c {count} попытки, поздравляем!')
            break


compare_num()
