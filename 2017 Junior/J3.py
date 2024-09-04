vals = input().split()
a, b = int(vals[0]), int(vals[1])
vals = input().split()
c, d = int(vals[0]), int(vals[1])
t = int(input())
s = abs(a-c) + abs(b - d)
if t >= s and t % 2 == s % 2:
    print("Y")
else:
    print("N")