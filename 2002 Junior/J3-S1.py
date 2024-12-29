p = int(input())
g = int(input())
r = int(input())
o = int(input())
amt = int(input())

cnt = 0
minimum = amt
for pink in range(amt+1):
    for green in range(amt+1):
        for red in range(amt+1):
            for orange in range(amt+1):
                total = pink * p + green * g + red * r + orange * o
                if total == amt:
                    print(f"# of PINK is {pink} # of GREEN is {green} # of RED is {red} # of ORANGE is {orange}")
                    cnt += 1
                    minimum = min(minimum, green + pink + red + orange)

print(f"Total combinations is {cnt}.")
print(f"Minimum number of tickets to print is {minimum}.")