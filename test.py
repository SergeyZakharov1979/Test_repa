num = int(input())

count = 0
for div in range(2, num + 1):
    if num % div == 0:
        count += 1
if count == 1:
    print(True)
else:
    print(False)