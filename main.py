s = input()
cnt = s.count('f')

if cnt == 1:
    print(s.find('f'))
elif cnt >= 2:
    print(s.find('f'), s.rfind('f'))
else:
    print('NO')
