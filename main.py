while True:
    n = int(input())

    for _ in range(n):
        cls = input()
        if len(cls) == 2:
            print('YES' if 48 <= ord(cls[0]) <= 57 and 1040 <= ord(
                cls[1]) <= 1055 else 'NO')
        else:
            print('NO')
