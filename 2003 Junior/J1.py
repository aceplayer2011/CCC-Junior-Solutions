bar = int(input())
space = int(input())
handle = int(input())

for i in range(bar):
    print("*" + " "*space + "*" + " "*space + "*")
print("*"*(space*2+3))
for i in range(handle):
    print(" "*(space+1) + "*")