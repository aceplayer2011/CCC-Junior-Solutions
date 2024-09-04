month = int(input())
day = int(input())
if month <= 1:
    print("Before")
elif month >=3:
    print("After")
else:
    if day <= 17:
        print("Before")
    elif day == 18:
        print("Special")
    else:
        print("After")