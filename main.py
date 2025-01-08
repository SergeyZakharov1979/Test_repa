n = int(input())
summ, cnt, mult, num = 0, 0, 1, n

while n > 0:
    last_num = n % 10

    summ += last_num
    cnt += 1
    mult *= last_num 

    n //= 10

f_num = num // (10**(cnt - 1))
l_num = num % 10
summ_fl = f_num + l_num
aver = summ / cnt

print(summ, cnt, mult, aver, f_num, summ_fl, sep='\n')
