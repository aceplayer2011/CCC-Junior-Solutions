w = int(input())
h = float(input())
bmi = w/(h*h)
if bmi > 25:
    print('Overweight')
elif bmi >= 18.5 and bmi <= 25:
    print('Normal weight')
else:
    print('Underweight')