prevtime = input().split(':')
h, m = int(prevtime[0]), int(prevtime[1])

for i in range(120):
    if 7 <= h < 10 or 15 <= h < 19:
        m += 2
    else:
        m += 1
    
    if m >= 60:
        h += 1
        m -= 60
    if h >= 24:
        h -= 24

if h < 10:
    sh = '0' + str(h)
else:
    sh = str(h)
if m < 10:
    sm = '0' + str(m)
else:
    sm = str(m)

print(sh + ':' + sm)