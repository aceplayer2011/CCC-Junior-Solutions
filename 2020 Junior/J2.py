P = int(input())
N = int(input())
R = int(input())
d = 0
i = N
while (i <= P):
    i += N*R
    N *= R
    d += 1
print(d)