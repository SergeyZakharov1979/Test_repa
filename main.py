n = input()
string, line_code = [], []

for st in range(int(n[1:])):
    string = input().split('#')
    line_code.append(string[0].rstrip())
    string.clear()

print(*line_code, sep='\n')

