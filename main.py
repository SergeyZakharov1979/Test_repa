n = int(input())

# for i in range(1, n // 2 + 2):
#     print('*' * i)

# for j in range(n // 2, 0, - 1):
#     print('*' * j)


cnt = n // 2

for _ in range(n):
    for _ in range(n // 2 - abs(cnt)):
        print('*', end='')
    print()
    cnt -= 1