n = int(input())

dm = []

for i in range(n):
    lines = input().split(" ")
    n = int(lines[0])
    symbol = lines[1]
    dm.append(symbol * n)

print(*dm, sep="\n")