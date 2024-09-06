t = input()
cnt = 0
H = 0
V = 0
for i in range(len(t)):
    if t[cnt] == "H":
        H += 1
    else:
        V += 1
    cnt += 1

if V % 2 == 0:
    if H % 2 == 0:
        print("1 2\n3 4")
    else:
        print("3 4\n1 2")
else:
    if H % 2 == 0:
        print("2 1\n4 3")
    else:
        print("4 3\n2 1")