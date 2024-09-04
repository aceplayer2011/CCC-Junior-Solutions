te = {54: 19, 90: 48, 99: 77, 9: 34, 40: 64, 67: 86}
pos = 1
while True:
    n = int(input())
    if n == 0:
        print("You Quit!")
        break
    elif pos + n == 100:
        print("You are now on square 100")
        print("You Win!")
        break
    elif pos + n < 100:
        pos += n
        if pos in te:
            pos = te[pos]
    print("You are now on square", pos)