# grades1 = {'Alice': 85, 'Bob': 90}
# grades2 = {'Charlie': 78, 'Diana': 92}
# grades1.update(grades2)
# print(grades1)
# print(len(grades1))
# *****************************************
# original = {'a': 1, 'b': 2, 'c': 3}
# new = {}
# for k, v in original.items():
#     new[v] =  k
# print(new)
# *****************************************
# students_grade, d = {}, {}
# name = ['Sergey', 'Marina', 'Ivan', 'Liza']
# discipline = ['Math', 'Phizic', 'Chemistry']
# d = dict.fromkeys(discipline)
# for n in name:
#     students_grade.setdefault(n, d)
# print(students_grade)
# *****************************************
# k = ['cat', 'dog', 'parrot']
# v = ['кошка', 'собака', 'попугай']
# animals = dict(zip(k, v))
# print(animals)
# *****************************************
# grades = {'Alice': 5, 'Bob': 4, 'Charlie': 3}
# # print(*(k for k in grades.keys()))
# print(*list(grades.keys()))
# *****************************************
# morse = {
#     'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..'
# }
# morse.setdefault('E', '.')
# print(morse)
# *****************************************
# grades = {'Alice': 5, 'Bob': 4, 'Charlie': 3, 'Diana': 5}
# grades.pop('Bob')
# del grades['Bob']
# print(grades)
# *****************************************
# nums = {'one': 1, 'two': 2, 'three': 3}
# print(*(nums.values()))
# *****************************************
# data = {'x': 10, 'y': 20, 'z': 30}
# del_value = data.pop('y')
# print(del_value)
# *****************************************
# info = {'name': 'Ivan', 'age': 25, 'city': 'Moscow'}
# for pare in info.items():
#     print(pare)
# *****************************************
# morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..'}
# if 'E' in morse:
#     print(f'ключ {'E'} есть в словаре')
# else:
#     morse.setdefault('E', '.')
#     print(f'ключ {'E'} был добавлен в словарь')
# *****************************************
# nums = {'one': 1, 'two': 2, 'three': 3}
# nums['two'] = nums.get('two') * 11
# print(nums)
# *****************************************
# letters = {'A': '.-', 'B': '-...', 'C': '-.-.'}
# print(*letters.values())
# *****************************************
# nums = {'one': 1, 'two': 2, 'three': 3}
# print(len(nums))
# *****************************************
# original = {'a': 1, 'b': 2, 'c': 3}
# original = {v: k for k,  v in original.items()}
# print(original)
# *****************************************
# d = {'a': 1, 'b': 2, 'c': 3}
# print(d.get('d', 0))
# *****************************************
# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45,
#          'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777,
#          'c': 12, 'p': 123, 'w': 111, 'z': 666}
# result = {}
# result = result | dict1

# for k1, v1 in dict1.items():
#     for k2, v2 in dict2.items():
#         if k2 in dict1 and k1 == k2:
#             result[k1] = v1 + v2
#         elif k2 in dict1 and k1 != k2:
#             continue
#         else:
#             result[k2] = v2
# *****************************************
# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# result = {}
# for c in text:
#     result[c] = result.get(c, 0) + 1

# print(result)
# *****************************************
# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
# d = {}
# for c in s.split():
#     d[c] = d.get(c, 0) + 1
# mx = max(d.values())
# res = [k for k, v in d.items() if v == mx]
# print(min(res))
# *****************************************
# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]

# result = {}
# for data in pets:
#     k = data[1:]
#     v = data[0]
#     if k not in result:
#         result[k] = result.get(k, [v])
#     else:
#         result.get(k).append(v)
# print(result)
# *****************************************
# s = [c.strip('.,!?:;-') for c in input().lower().split()]
# d = {}
# for k in s:
#     d[k] = d.get(k, 0) + 1
# mn = min(d.values())
# result = (k for k, v in d.items() if v == mn)
# print(min(result))
# ******************************************
