grid = ['ABCDEF', 'GHIJKL', 'MNOPQR', 'STUVWX', 'YZ -.']

def get_rc(ch):
    for ir, row in enumerate(grid):
        for ic, v in enumerate(row):
            if ch == v:
                return (ir, ic)

s = input()
cnt = 0
pr, pc = 0, 0
for ch in s:
    r, c = get_rc(ch)
    cnt += abs(r-pr) + abs(c-pc)
    pr, pc = r, c
cnt += abs(4-pr) + abs(5-pc)
print(cnt)