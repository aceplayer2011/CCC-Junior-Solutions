s = int(input())
ys = input()
ts = input()
c = 0
for i in range(0, s):
    if ys[i] == "C" and ts[i] == "C":
        c += 1
print(c)