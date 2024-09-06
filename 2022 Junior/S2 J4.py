X = int(input())
Fs = []
for i in range(X):
    a, b = input().split()
    Fs.append((a, b))
Y = int(input())
Es = []
for i in range(Y):
    a, b = input().split()
    Es.append((a, b))
G = int(input())
gs = {}
for i in range(G):
    gp =  input().split()
    for x in gp:
        gs[x] = i
cnt = 0
for f in Fs:
    a, b = f[0], f[1]
    if gs[a] != gs[b]:
        cnt += 1
for e in Es:
    a, b = e[0], e[1]
    if gs[a] == gs[b]:
        cnt += 1
print(cnt)