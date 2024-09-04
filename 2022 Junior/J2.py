p = int(input())
c = 0
g = ""
for i in range(p):
    pts = (5*int(input())) - (3*int(input()))
    if pts > 40:
        c+=1
if c == p:
    g ="+"
print(str(c)+g)