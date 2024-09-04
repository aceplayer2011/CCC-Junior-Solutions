n = int(input())
ans = 1
while ans*ans <= n:
    ans += 1
ans -= 1
print("The largest square has side length " + str(ans)+'.')