s = input()
frq_repit_smbl = ''
cnt_frq_repit_smbl = 0

while len(s) > 0:
    cur_symb = s[0]
    cnt_cur_symb = s.count(s[0])

    if cnt_cur_symb >= cnt_frq_repit_smbl:
        cnt_frq_repit_smbl = cnt_cur_symb
        frq_repit_smbl = cur_symb

    s = s.replace(cur_symb, '')

print(frq_repit_smbl)
