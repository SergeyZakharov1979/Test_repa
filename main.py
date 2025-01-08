n, flag = int(input()), 'YES'
last_num = n % 10

while n > 0:
    curent_num = n % 10

    if curent_num != last_num:
        flag = 'NO' 
        break
    else:
        n //= 10

print(flag)
