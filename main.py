n = input()
letters = 'АВЕКМНОРСТУХ'

seria = n[0] + n[4:6]
number = n[1:4]
region = n[7:9]
new_region = n[7:10]

for c in seria:
    if c not in letters:
        print('NO')
        break
else:
    if len(n) == 9 and number.isdigit() and region.isdigit() and n[6] == '_':
        flag = 'YES'
    elif len(n) == 10 and number.isdigit() and new_region.isdigit() and n[6] == '_':
        flag = 'YES'
    else:
        flag = 'NO'

    print(flag)