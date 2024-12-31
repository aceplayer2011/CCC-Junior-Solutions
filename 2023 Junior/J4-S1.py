num = int(input())
row1 = input().replace(" ", "")
row2 = input().replace(" ", "")

tapes = 0
borw1, borw2 = 'w', 'w'


for i in range(num):
    topbottom = 0 

    if row1[i] == '1':
        if borw1 == 'w':
            tapes += 3
        else:
            tapes += 1
        borw1 = 'b'
        topbottom += 1
    else:
        borw1 = 'w'

    if row2[i] == '1':
        if borw2 == 'w':
            tapes += 3
        else:
            tapes += 1
        borw2 = 'b'
        topbottom += 1
    else:
        borw2 = 'w'

    if i%2 == 0:
        if topbottom == 2:
            tapes -= 2

print(tapes)