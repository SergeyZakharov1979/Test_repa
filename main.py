n = int(input())

while n > 0:
    last_num = n % 10
    print(last_num)
    n //= 10