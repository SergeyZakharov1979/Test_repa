n = int(input())
seq_x, seq_F = [], []

for i in range(n):
    x = int(input())
    seq_x.append(x)
    F = pow(x, 2) + 2*x + 1
    seq_F.append(F)

print(*seq_x, sep='\n')
print()
print(*seq_F, sep='\n')
