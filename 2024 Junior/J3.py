a = int(input())
count = 0
score = []

for i in range(a):
    t = int(input())
    score.append(t)
score.sort(reverse=True)

bronze = sorted(set(score), reverse=True)[2]

for z in range(a):
    if score[z] == bronze:
        count += 1

print(bronze, count)