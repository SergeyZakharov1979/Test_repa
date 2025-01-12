n = int(input())

for i in range(1, n + 1):
    cur_div = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cur_div +=1

    print(str(i) + '+' * cur_div)