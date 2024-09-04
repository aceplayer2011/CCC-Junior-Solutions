a = int(input())
b = int(input())
c = int(input())
t = a + b + c
tritype = ""
if t == 180:
    if a == b or b == c or a == c:
        tritype = "Isosceles"
        if a == b == c:
            tritype = "Equilateral"
    else:
            tritype = "Scalene"
else: 
            tritype = "Error"

print(tritype)