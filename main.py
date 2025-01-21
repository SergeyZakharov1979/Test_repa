while True:
    str1, str2 = input().lower(), input().lower()
    cnt1, cnt2 = 0, 0

    for c in str1:
        if c.isalpha():
            cnt1 += ord(c)

    for c in str2:
        if c.isalpha():
            cnt2 += ord(c)

    print('YES' if cnt1 == cnt2 else 'NO')