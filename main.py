w = input()
small = w
large = w

for _ in range(2):
    w = input()
    if w < small:
        small, w = w, small
    if w > large:
        large, w = w, large

print(small, w, large)