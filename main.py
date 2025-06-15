a, b = int(input()), int(input())

while a <= b:
    if a % 777 == 0:
        break
    if a % 2 == 0 or a % 3 == 0:
        a += 1
        continue
    print(a)
    a += 1
