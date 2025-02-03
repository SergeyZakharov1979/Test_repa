a = [7, 3, 9, 2, 1, 0]
n = len(a)

for i in range(n - 1):
    #  a[:(n - i)]
    mx = max(a[:(n - i)])
    ind_mx = a[:(n - i)].index(mx)
    ind_cur = n -1 - i

    a[ind_mx], a[ind_cur] = a[ind_cur], a[ind_mx]


print(a)
