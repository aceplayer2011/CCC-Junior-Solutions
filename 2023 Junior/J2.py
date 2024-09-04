a = int(input())
cnt = 0
for i in range(a):
    b = input()
    if b == "Poblano":
        cnt += 1500
    elif b == "Mirasol":
        cnt += 6000
    elif b == "Serrano":
        cnt += 15500
    elif b == "Cayenne":
        cnt += 40000
    elif b == "Thai":
        cnt += 75000
    elif b == "Habanero":
        cnt += 125000
print(cnt)