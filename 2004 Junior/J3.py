a = int(input())
b = int(input())
acnt = 0
bcnt = 0
alist = []
blist = []
for i in range(a):
    alist.append(input(""))
for c in range(b):
    blist.append(input(""))
for u in range(a):
    for d in range(b):
        print(alist[acnt], "as", blist[bcnt])
        bcnt += 1
    acnt += 1
    bcnt = 0