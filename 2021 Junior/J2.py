n = int(input())
w = ""
hb = 0
for i in range(n):
    n1 = input()
    b = int(input())
    if b > hb:
        w = n1
        hb = b
print(w)