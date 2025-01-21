
n = int(input())

book = input().split(maxsplit=2)
autor = book[0]
title = book[2]
flag = "YES"
print(autor, title)
for _ in range(n - 1):
    book = input().split(maxsplit=2)
    print(book)
    if book[0] > autor:
        continue
    elif book[0] == autor:
        if book[2] > title:
            continue
        else:
            flag = 'NO'
            break
    else:
        flag = 'NO'
        break
print(flag)