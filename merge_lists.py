def merge_list(lst1, lst2):
    rezult = []
    p1, p2 = 0, 0
    while p1 < len(lst1) and p2 < len(lst2):

        if lst1[p1] < lst2[p2]:
            rezult.append(lst1[p1])
            p1 += 1
        else:
            rezult.append(lst2[p2])
            p2 += 1

    if p1 < len(lst1):
        rezult.extend(lst1[p1:])
    elif p2 < len(lst2):
        rezult.extend(lst2[p2:])

    return rezult
