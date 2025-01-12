a, b = int(input()), int(input())
max_div, summ, cur_summ = 1, 1, 0

for i in range(a, b + 1):
    cur_summ = 0
    for j in range(1, b + 1):
        if i % j == 0:
            cur_summ +=j

    if cur_summ >= summ:
        max_div = i
        summ = cur_summ

print(max_div, summ)