n = int(input())
dig_root = n

while dig_root > 9:
    n = dig_root 
    dig_root = 0

    while n > 0:
        last_dig = n % 10
        dig_root += last_dig
        n //= 10
        
print(dig_root)