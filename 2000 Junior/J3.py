q = int(input())
m1 = int(input())
m2 = int(input())
m3 = int(input())

t = 0
while q > 0:
    t += 1
    q -= 1
    m1 += 1
    if m1 == 35:
        q += 30
        m1 = 0
    if q == 0:
        break
    t += 1
    q -= 1
    m2 += 1
    if m2 == 100:
        q += 60
        m2 = 0
    if q == 0:
        break
    t += 1
    q -= 1
    m3 += 1
    if m3 == 10:
        q += 9
        m3 = 0
        
print("Martha plays", t, "times before going broke.")