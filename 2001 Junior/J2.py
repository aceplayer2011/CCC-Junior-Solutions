from sys import stdin
input = stdin.readline

a = int(input())
b = int(input())

def exist():
    for i in range(1, b):
        if (a*i) % b == 1:
            return i
    return("No such integer exists.")

print(exist())