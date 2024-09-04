sl = int(input())
cs = int(input())
if cs<=sl:
    print("Congratulations, you are within the speed limit!")
elif cs>sl:
    sf1 = cs-sl
    if sf1<=20:
        print("You are speeding and your fine is $100.")
    elif sf1<=30 and sf1>=21:
        print("You are speeding and your fine is $270.")
    elif sf1>=31:
        print("You are speeding and your fine is $500.")