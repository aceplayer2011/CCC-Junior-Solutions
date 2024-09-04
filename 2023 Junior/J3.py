dict1 = {1:0,2:0,3:0,4:0,5:0}
for t in range(int(input())):
    l = input()
    for p in range(len(l)):
        if l[p]=='Y':
            dict1[p+1]+=1
l = []
p = list(dict1.values())
k = max(p)
for t in range(5):
    if p[t]==k:
        l.append(str(t+1))
if len(l)==1:
    print(l[0])
else:
    print(','.join(l))