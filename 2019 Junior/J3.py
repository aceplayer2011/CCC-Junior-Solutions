new = -1
sequences = []
lines = int(input())

for i in range(lines):
    sequences.append(input())

for i in range(lines):
    for j in range(len(sequences[i])):
        if j < (len(sequences[i]) - 1):
            if sequences[i][j] != sequences[i][j+1]:
                print(j - new, sequences[i][j], end=" ")
                new = j
        else:
            print(j - new, sequences[i][j])
    new = -1