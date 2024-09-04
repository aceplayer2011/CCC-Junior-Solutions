v = [0, 0]

def map(x):
    if x == 'A':
        return 0
    else:
        return 1

while True:
    vals = input().split()
    op = int(vals[0])
    if op == 7:
        break
    ix = map(vals[1])
    x = vals[1]
    if op == 1:
        n = int(vals[2])
        v[ix] = n
    elif op == 2:
        print(v[ix])
    else:
        iy = map(vals[2])
        if op == 3:
            v[ix] = v[ix] + v[iy]
        elif op == 4:
            v[ix] = v[ix] * v[iy]
        elif op == 5:
            v[ix] = v[ix] - v[iy]
        else:
            v[ix] = v[ix] // v[iy]