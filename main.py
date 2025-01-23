lst = []
for i in range(26):
    j = i + 1
    lst.append(chr(ord('a') + i) * j)

print(lst)