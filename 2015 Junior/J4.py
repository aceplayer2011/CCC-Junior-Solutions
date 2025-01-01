M = int(input())
time = 0
d = {}

preOp = ''
for _ in range(M):
    vals = input().split()
    op, X = vals[0], int(vals[1])
    if op == 'W':
        time += X
    else:
        if preOp == 'R' or preOp == 'S':
            time += 1
        if X in d:
            d[X].append(time)
        else:
            d[X] = [time]
    preOp = op

for X, times in sorted(d.items()):
    if len(times) % 2 == 1:
        print(X, -1)
    else:
        t = 0
        for i in range(0, len(times), 2):
            t += times[i+1]-times[i]
        print(X, t)