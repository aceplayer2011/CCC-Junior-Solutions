N = int(input())
a = []
for _ in range(N):
    vals = input().split()
    a.append(vals)
v = [int(a[0][0]), int(a[0][-1]), int(a[-1][0]), int(a[-1][-1])]
sml = min(v)
rotation = 0
if v[1] == sml:
    rotation = 3
elif v[2] == sml:
    rotation = 1
elif v[3] == sml:
    rotation = 2
for _ in range(rotation):
    a = list(zip(*a[::-1]))
for r in a:
    print(*r)