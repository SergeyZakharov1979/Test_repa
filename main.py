n = int(input())
maximum = 0
minimum = 10**30

while n > 0:
    last_num = n % 10

    if last_num > maximum:
        maximum = last_num
    if last_num < minimum:
        minimum = last_num

    n //= 10

print(f'Максимальная цифра равна {maximum}', f'Минимальная цифра равна {minimum}', sep='\n')
