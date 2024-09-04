a = int(input())
b = int(input())
c = int(input())
tl = int(input())
cnt = 0
for i in range(0, tl // a + 1):
    for j in range(0, tl // b + 1):
        for k in range(0, tl // c + 1):
            if i + j + k > 0 and i * a + j * b + k * c <= tl:
                print(f"{i} Brown Trout, {j} Northern Pike, {k} Yellow Pickerel")
                cnt += 1
print(f"Number of ways to catch fish: {cnt}")