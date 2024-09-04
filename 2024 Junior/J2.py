dusasize = int(input())

while True:
    n = int(input())
    if dusasize > n:
        dusasize += n
    else:
        break
print(dusasize)