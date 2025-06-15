# Камень ножницы бумага
def rock_paper_scissors(i, j):
    if i == j:
        return 0
    elif (i == 0 and j == 1) or (i == 1 and j == 2) or (i == 2 and j == 0):
        return 1
    else:
        return 2


toys = ['камень', 'ножницы', 'бумага']
players = ['ничья', 'Тимур', 'Руслан']

i = toys.index(input())
j = toys.index(input())

print(players[rock_paper_scissors(i, j)])


# Камень ножницы бумага ящерица Спок
table = [
    [0, 1, 2, 1, 2],
    [2, 0, 1, 1, 2],
    [1, 2, 0, 2, 1],
    [2, 2, 1, 0, 1],
    [1, 1, 2, 2, 0]
]

toys = ['камень', 'ножницы', 'бумага', 'ящерица', 'Спок']
players = ['ничья', 'Тимур', 'Руслан']

i = toys.index(input())
j = toys.index(input())

ind_res = table[i][j]

print(players[ind_res])
