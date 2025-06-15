from random import randrange
def input_matrix(N: int):
    matrix = []
    for _ in range(N):
        matrix.append([int(_) for _ in input().split()])
    return matrix


def change_matrix_task_1(matrix: list):
    for i in range(N // 2):
        matrix[i], matrix[N - 1 - i] = matrix[N - 1 - i], matrix[i]

    for i in range(N):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


def output_matrix(matrix: list):
    for row in matrix:
        print(*row)


# m = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

N = int(input())
m = input_matrix(N)
m = change_matrix_task_1(m)
output_matrix(m)

# ****************************************


def matrix_input(N: int):
    sq = [[int(_) for _ in input().split()] for _ in range(N)]
    return sq


def matrix_random(N: int):
    matrix = [[randrange(1, 9) for _ in range(N)] for _ in range(N)]
    return matrix


def matrix_transpose(matrix: list):
    result = [[0] * len(matrix) for _ in range(len(matrix[0]))]

    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            result[i][j] = matrix[j][i]

    return result


def output_matrix(matrix: list):
    for row in matrix:
        print(*row)


def test_number(matrix: list):
    N = len(matrix)
    sample_list = list(range(1, N**2 + 1))
    test_list = []

    for i in range(N):
        for j in range(N):
            test_list.append(matrix[i][j])

    return sample_list == sorted(test_list)


def is_magic(square: list):
    flag = 'YES'
    s = sum(square[0])

    # проверка квадрата на повторяющиеся цифры
    if not test_number(square):
        flag = 'NO'

    # проверка сумм строк
    for row in square:
        if sum(row) != s:
            flag = 'NO'
            break

    # проверка суммы главной диагонали
    sum_mn_diag = 0
    N = len(square)
    for i in range(N):
        sum_mn_diag += square[i][i]

    if sum_mn_diag != s:
        flag = 'NO'

    # проверка суммы побочной диагонали
    sum_sec_diag = 0
    N = len(square)
    for i in range(N):
        sum_sec_diag += square[i][N - 1 - i]

    if sum_sec_diag != s:
        flag = 'NO'

    square = matrix_transpose(square)

    # проверка сумм столбцов
    for row in square:
        if sum(row) != s:
            flag = 'NO'
            break

    return flag


N = int(input())
sq = matrix_input(N)
print(is_magic(sq))


#*****************************************

def creating_a_matrix_template(N: int, M: int):
    matrix = [[0] * M for _ in range(N)]
    return matrix


def creating_a_matrix_template2(N: int):
    matrix = [[0] * N for _ in range(N)]
    return matrix


def output_matrix(matrix: list):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(str(matrix[row][col]).rjust(3), end='')
        print()


def output_matrix2(matrix: list):
    for row in matrix:
        print(*row)


def filling_the_matrix(matrix: list):
    N = len(matrix)
    for i in range(N):
        for j in range(M):
            matrix[i][j] = ((i + j) * (i + j + 1)) // 2 + i + 1
    return matrix


N, M = map(int, input().split())
m = creating_a_matrix_template(N, M)
m = filling_the_matrix(m)
output_matrix(m)


#************************************************** Умножение матриц
def input_matrix(N: int, M: int):
    matrix = [[int(_) for _ in input().split()] for _ in range(N)]
    return matrix


def matrix_template(N: int, M: int):
    m3 = [[0] * M for _ in range(N)]
    return m3


def output_matrix(matrix: list):
    for row in matrix:
        print(*row)


def summation_matrix(m1: list, m2: list):
    matrix3 = []
    for i in range(N):
        row = []
        for j in range(M):
            cur_el = m1[i][j] + m2[i][j]
            row.append(cur_el)
        matrix3.append(row)
    return matrix3


def matrix_multiplication(m1: list, m2: list):
    m3 = []

    row = []
    for i in range(N):
        value_cur_el = 0
        for j in range(K):
            value_cur_el += m1[i][j] * m2[j][i]
        row.append(value_cur_el)
    m3.append(row)
    return m3


N, M = map(int, input().split())
m1 = input_matrix(N, M)
input()
M, K = map(int, input().split())
m2 = input_matrix(M, K)

m3 = matrix_multiplication(m1, m2)
output_matrix(m3)
