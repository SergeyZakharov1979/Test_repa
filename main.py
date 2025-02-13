def is_correct_bracket(text):
        stack = 0
        for brkt in text:
            if stack < 0:
                return False
            if brkt == '(':
                stack += 1
            elif brkt == ')':
                stack -= 1
                
        return stack == 0


for i in range(16):
    text = input()
    print(is_correct_bracket(text))
