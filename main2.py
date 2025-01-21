s = input()
new_s = ''
while s != '':
    if s[0] != '[':
        new_s += s[0]
        s = s[1:]
    else:
        code = ''
        while s[0] != ']':
            if s[0] in '0123456789':
                code += s[0]
            s = s[1:]
        new_s += chr(int(code)) 
        s = s[1:]

print(new_s)