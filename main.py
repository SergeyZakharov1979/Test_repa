s, cnt_vowels, cnt_consonants = input(), 0, 0
volwels, consonants = 'ауоыиэяюе', 'бвгджзйклмнпрстфхцчшщ'

for c in s:
    if c.lower() in volwels:
        cnt_vowels += 1
    if c.lower() in consonants:
        cnt_consonants += 1
    
print(f'Количество гласных букв равно {cnt_vowels}')
print(f'Количество согласных букв равно- {cnt_consonants}')

