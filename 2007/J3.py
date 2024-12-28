v = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
n = int(input())
for i in range(n):
    idx = int(input())
    v[idx-1] = 0
avg = sum(v) / (10-n)
offer = int(input())
if offer > avg:
    print("deal")
else:
    print("no deal")