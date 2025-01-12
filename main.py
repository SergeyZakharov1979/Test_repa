n = int(input())

for i in range(n):
    cnt = 0
    for j in range(i + 1):
        cnt +=1
        print(cnt, end='')

    for k in range(i, 0, - 1):
        cnt -= 1
        print(cnt, end='')
    print()