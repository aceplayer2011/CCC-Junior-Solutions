word = input()
flag = True
for i in range(len(word)):
    if word[i] != "I" and word[i] != "O" and word[i] != "S" and word[i] != "H" and word[i] != "Z" and word[i] != "X"\
    and word[i] != "N":
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")