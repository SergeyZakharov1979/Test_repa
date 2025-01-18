cur_day, cur_weight = int(input()), float(input())

control_weight = 100 - 0.2 * cur_day

if cur_weight > control_weight:
    mess = 'Что-то пошло не так'
else:
    mess = 'Все идет по плану'

print(f'''{mess}
#{cur_day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {cur_weight} кг, ЦЕЛЬ по ВЕСУ = {control_weight} кг
''')