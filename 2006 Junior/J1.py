burger = [0, 461, 431, 420, 0]
side = [0, 100, 57, 70, 0]
drink = [0, 130, 160, 118, 0]
dessert = [0, 167, 266, 75, 0]

a = int(input())
b = int(input())
c = int(input())
d = int(input())
cals = 0
cals += burger[a]
cals += side[b]
cals += drink[c]
cals += dessert[d]
 
print("Your total Calorie count is " + str(cals) + ".")