s, cnt = input(), 0

while len(s) > 0:
    if s[-1].isalpha():
        if s[-1] == s[-1].lower():
            cnt += 1
    s = s[:-1]

print(cnt)