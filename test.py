# def test_number(matrix: list):
#     N = len(matrix)
#     sample_list = list(range(1, N**2))
#     test_list = []

#     for i in range(N):
#         for j in range(N):
#             test_list.append(matrix[i][j])

#     return sample_list == sorted(test_list)

# m = [
#     [8, 1, 6],
#     [3, 5, 7],
#     [4, 9, 2]
# ]

# print(test_number(m))

N = int(input())
sample_list = list(range(1, N**2 + 1))
print(sample_list)
