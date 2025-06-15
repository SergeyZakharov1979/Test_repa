lst = input().split()
res = [[]]
cnt = len(lst)
for i in range(1, len(lst) + 1):
    cnt -= 1
    j = 0
    while j <= cnt:
        res.append(lst[j:j + i])
        j += 1
print(res)
