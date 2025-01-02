a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())
sln = s
slb = s
ns = 0
bs = 0
doneornot = 0
while True:
    if (sln - a) > 0:
        sln -= a
        ns += a
    else:
        ns += sln
        doneornot += 1
        sln = 0
    if (sln - b) > 0:
        sln -= b
        ns -= b
    else:
        ns -= sln
        doneornot += 1
    
    
    if (slb - c) > 0:
        slb -= c
        bs += c
    else:
        bs += slb
        doneornot += 1
        slb = 0
    if (slb - d) > 0:
        slb -= d
        bs -= d
    else:
        bs -= slb
        doneornot += 1
    
    if doneornot >= 1:
        break


if ns > bs:
    print("Nikky")
elif ns == bs:
    print("Tied")
else:
    print("Byron")