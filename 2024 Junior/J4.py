num = int(input())
for3points = input()
trash = input()
cnt = 0
tapes = 0

for i in range(len(for3points)):
    if for3points[cnt] == '1':
        tapes += 3
    cnt += 1
'''
while True:
    if cnt == num:
        break
    else:
        if for3points[cnt] == '1':
            tapes += 3
        cnt += 1
'''
print(tapes)