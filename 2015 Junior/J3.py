c = "bcdfghjklmnpqrstvwxyz"
cv = "aaeeeiiiiooooouuuuuuu"
nc = "cdfghjklmnpqrstvwxyzz"

word = input()
neww = ""
for x in word:
    j = c.find(x)
    neww += x
    if j > -1:
        neww = neww + cv[j] + nc[j]
print(neww)