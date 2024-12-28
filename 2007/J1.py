one = int(input())
two = int(input())
three = int(input())

if one > two and one < three:
    print (one)
elif one > three and one < two:
    print(one)
elif two > one and two < three: 
    print(two)
elif two > three and two < one:
    print(two)
elif three > one and three < two:
    print(three)
elif three > two and three < one:
    print(three)