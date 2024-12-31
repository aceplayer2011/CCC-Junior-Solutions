D = int(input())
sequences = [34, 
             111, 123, 135 ,147, 159,
             210, 222, 234, 246, 258,
             321, 333, 345, 357,
             420, 432, 444, 456,
             531, 543, 555,
             630, 642, 654,
             741, 753,
             840, 852,
             951,
             1111]


c1 = D//720
t1 = c1 * len(sequences)
h, m = (D % 720)//60, D % 60
rem = h * 100 + m
t2 = 0
for seq in sequences:
    if seq <= rem:
        t2 += 1
    else:
        print(t1+t2)
        break