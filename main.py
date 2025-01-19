s = input()
en_let = 'eyopaxcETOPAHXCBM'
ru_let = 'еуорахсЕТОРАНХСВМ'

old_cost, new_cost = 0, 0

for c in s:
    old_cost += ord(c) * 3
    if c in en_let:
        new_cost += ord(ru_let[en_let.find(c)]) * 3
    else:
        new_cost += ord(c) * 3

print(f'Старая стоимость: {old_cost}🐝', f'Новая стоимость: {new_cost}🐝', sep='\n')
