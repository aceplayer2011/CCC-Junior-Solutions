a, b, c, d, e, f = input(), input(), input(), input(), input(), input()
cnt = 0
groupnum = 0

if a == "W":
    cnt += 1
if b == "W":
    cnt += 1
if c == "W":
    cnt += 1
if d == "W":
    cnt += 1
if e == "W":
    cnt += 1
if f == "W":
    cnt += 1

if cnt == 5 or cnt == 6:
    groupnum = 1
if cnt == 3 or cnt == 4:
    groupnum = 2
if cnt == 1 or cnt == 2:
    groupnum = 3
if cnt == 0:
    groupnum = -1

print(groupnum)