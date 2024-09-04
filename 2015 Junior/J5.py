n = int(input())
k = int(input())
pimap = dict()
def pi(pieces, people):
    if pieces < people:
        return 0
    if people == 1 or pieces == people:
        return 1
    if (pieces, people) in pimap:
        return pimap[(pieces, people)]
    pimap[(pieces, people)] = pi(pieces - 1, people - 1) + pi(pieces - people, people)
    return pimap[(pieces, people)]


print(pi(n, k))