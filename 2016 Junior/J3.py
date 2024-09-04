s = input()
ans = 1
n = len(s)

def palchecker(x):
    return x == x[::-1]

for i in range(n):
    for j in range(i, n):
        if palchecker(s[i:j+1]):
            ans = max(ans, j-i+1)
print(ans)