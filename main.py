def determining_the_day_of_the_week(n):
    week = ['понедельник', 'вторник', 'среда',
            'четверг', 'пятница', 'суббота', 'воскресенье']
    
    return week[(n % 7) - 1]

n = int(input())
print(determining_the_day_of_the_week(n))