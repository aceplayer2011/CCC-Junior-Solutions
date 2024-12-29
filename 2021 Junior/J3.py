while True:
    v = int(input())
    if v == 99999:
        break
    d1 = v // 10000
    d2 = (v % 10000) // 1000
    if d1 + d2 > 0:
        if (d1 + d2) % 2 == 1:
            direction = 'left'
        else:
            direction = 'right'
    print(direction, v % 1000)