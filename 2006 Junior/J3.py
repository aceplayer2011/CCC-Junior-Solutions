data = []
while True:
    x = input()
    if x == "halt":
        break
    else:
        data.append(x)

vls = {"a": "2", "b": "22", "c": "222", "d": "3", "e": "33", "f": "333", "g": "4", "h": "44", "i": "444", "j": "5", "k": "55", "l": "555", "m": "6", "n": "66", "o": "666", "p": "7", "q": "77", "r": "777", "s": "7777", "t": "8", "u": "88", "v": "888", "w": "9", "x": "99", "y": "999", "z": "9999"}

for i in range(0, len(data)):
    cnt = 0
    word = data[i]
    for x in range(0, len(word)):
        if x == 0:
            cnt += len(vls[word[x]])
        elif (vls[word[x]])[0] == (vls[word[x-1]])[0]:
            cnt += 2
            cnt += len(vls[word[x]])
        else:
            cnt += len(vls[word[x]])
    print(cnt)