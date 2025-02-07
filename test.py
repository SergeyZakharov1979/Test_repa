s = [1, 2, 1, 3]
n = len(s)
for i in range(n - 1):
    mx = max(s[:n - i])
    ind_mx = s[:n - i].index(mx)
    ind_cur = n - 1 - i

    s[ind_cur], s[ind_mx] = s[ind_mx], s[ind_cur]
print(s)
