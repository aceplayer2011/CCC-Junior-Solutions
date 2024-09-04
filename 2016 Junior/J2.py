tl = []
t0 = 0
t1 = 0
t2 = 0
t3 = 0
for i in range(1, 5):
    total = 0
    line = input()
    list = line.split()
    t0 += int(list[0])
    t1 += int(list[1])
    t2 += int(list[2])
    t3 += int(list[3])
    for i in range(0, len(list)):
        total += int(list[i])
    tl.append(total)
tl.append(t0)
tl.append(t1)
tl.append(t2)
tl.append(t3)
c = 0
for j in range(0, len(tl) - 1):
    if not tl[j] == tl[j + 1]:
        c += 1
if c == 0:
    print("magic")
else:
    print("not magic")