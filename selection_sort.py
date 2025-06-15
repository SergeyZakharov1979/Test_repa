# объявление функции
def merge(list1, list2):
    sm_lst = list1 + list2
    n = len(sm_lst)

    for i in range(n - 1):
        mx = max(sm_lst[:n - i])
        ind_mx = sm_lst[:n - i].index(mx)
        ind_cur = n - 1 - i

        sm_lst[ind_cur], sm_lst[ind_mx] = sm_lst[ind_mx], sm_lst[ind_cur]

    return sm_lst


# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))
