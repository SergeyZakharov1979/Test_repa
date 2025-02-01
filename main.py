a = [5, 1, 4, 2, 8]
cnt = 0

while cnt != len(a) - 1:
    for i in range(1, len(a)):
        if a[i-1] > a[i]:
            a[i], a[i-1] = a[i-1], a[i] 
    cnt += 1

print(a)