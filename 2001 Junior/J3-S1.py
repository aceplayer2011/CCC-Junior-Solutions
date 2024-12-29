cards = input()
idx_d = cards.find('D')
idx_h = cards.find('H')
idx_s = cards.find('S')
cs = list(cards[1:idx_d])
ds = list(cards[idx_d+1: idx_h])
hs = list(cards[idx_h+1: idx_s])
ss = list(cards[idx_s+1:])


def count_pts(suit):
    pts = 0
    if 'A' in suit:
        pts += 4
    if 'K' in suit:
        pts += 3
    if 'Q' in suit:
        pts += 2
    if 'J' in suit:
        pts += 1
    if len(suit) == 0:
        pts += 3
    elif len(suit) == 1:
        pts += 2
    elif len(suit) == 2:
        pts += 1
    return pts

print("Cards Dealt              Points")
pc = count_pts(cs)
pd = count_pts(ds)
ph = count_pts(hs)
ps = count_pts(ss)
print("Clubs", *cs, pc)
print("Diamonds", *ds, pd)
print("Hearts", *hs, ph)
print("Spades", *ss, ps)
print(f"                       Total {pc+pd+ph+ps}")