no_of_voters = int(input())
votelist = input()
voteA = 0
voteB = 0
for vote in (votelist):
    if vote == 'A':
        voteA += 1
    else:
        voteB += 1
if voteA > voteB:
    print("A")
elif voteA == voteB:
    print("Tie")
else:
    print("B")