x = int(input())
y = int(input())
a = int(input())
b = int(input())
if x < y and y < a and a < b:
  print("Fish Rising")
elif x > y and y > a and a > b:
  print("Fish Diving")
elif x==y and y==a and a==b:
  print("Fish At Constant Depth")
else:
  print("No Fish")