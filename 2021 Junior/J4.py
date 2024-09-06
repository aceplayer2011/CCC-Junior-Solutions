shelf = input()
def get_count(shelf : str) -> list:
    count = [0, 0, 0]
    for book in shelf:
        if book == 'L':
            count[0] += 1
        elif book == 'M':
            count[1] += 1
        else:
            count[2] += 1
    return count
L_total_count, M_total_count, S_total_count= get_count(shelf)
L = get_count(shelf[:L_total_count])
M = get_count(shelf[L_total_count:L_total_count+M_total_count])
S = get_count(shelf[L_total_count+M_total_count:])
single = min(L[1], M[0]) + min(L[2],S[0]) +min(M[2],S[1])
s = 0
if L[1] < M[0]:
    s = L[1]
else:
    s = M[0]
L[1] -= s
M[0] -= s
L[0] += s
M[1] += s
s = 0
if L[2] < S[0]:
    s = L[2]
else:
    s = S[0]
L[2] -= s
S[0] -= s
L[0] += s
S[2] += s
s = 0
if M[2] < S[1]:
    s = M[2]
else:
    s = S[1]
M[2] -= s
S[1] -= s
M[1] += s
S[2] += s
double = 2* (L[1] + L[2])
print(single+double)