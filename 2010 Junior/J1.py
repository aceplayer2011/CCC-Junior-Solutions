a = int(input())

if a < 6:
    out = a // 2 + 1
else:
    b = 5
    c = a - 5
    out = 1
    for i in range(a//2):
        b -= 1
        c += 1
        if c > b:
            break
        out += 1
print(out)