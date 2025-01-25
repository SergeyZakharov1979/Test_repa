n = int(input())
seq = []

for _ in range(n):
    seq.append(input())

k = int(input())
reqs = []

for _ in range(k):
    reqs.append(input())


for s in seq:
    cnt = 0
    for i in range(len(reqs)):
        if reqs[i].lower() in s.lower():
            cnt += 1
    if cnt == k:
        print(s)
