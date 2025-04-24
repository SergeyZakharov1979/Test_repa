def gcd(a, b):
    a, b = abs(a), abs(b)
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def least_common_multiple(a, b):
    return int((a * b) / gcd(a, b))


a, b = [int(input()) for i in range(2)]
print(least_common_multiple(a, b))
