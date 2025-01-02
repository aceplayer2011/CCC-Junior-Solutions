while True:
    vals = [int(x) for x in input().split()]
    n = vals[0]
    if n == 0:
        break
    elif n == 1:
        print(0)
    else:
        sequences = vals[1:]
        differences = []
        for i in range(1, n):
            differences.append(sequences[i]-sequences[i-1])
        for length in range(1, len(differences) + 1):
            pattern = differences[:length]
            isMatch = True
            for k in range(length, len(differences)):
                if (differences[k] != pattern[k%length]):
                    isMatch = False
                    break
            if isMatch:
                print(length)
                break