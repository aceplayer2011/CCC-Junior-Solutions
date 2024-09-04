m = int(input())
n = int(input())
count = 0

for i in range(1, m+1):
    if 10 - i in range(1, n+1):
        count += 1

if count != 1:
    print("There are %s ways to get the sum 10." % count)
else:
    print("There is %s way to get the sum 10." % count)