while True:
    hardest_word, summ_hard = '', 0

    for _ in range(4):
        wrd = input()
        cur_summ = 0
        for c in wrd:
            cur_summ += ord(c)

        if cur_summ > summ_hard:
            summ_hard = cur_summ
            hardest_word = wrd

    print(hardest_word)
    print()