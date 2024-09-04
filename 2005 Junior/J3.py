ins = []
while True:
    ic = input()
    if ic == "SCHOOL":
        break
    else:
        ins.append(ic)
ins.reverse()
ic = 0
while True:
    if ic == len(ins)-1:
        if ins[ic] == "R":
            print("Turn LEFT into your HOME.")
            break
        else:
            print("Turn RIGHT into your HOME.")
            break
    else:
        if ins[ic] == "R":
            print("Turn LEFT onto %s street." % ins[ic+1])
        else:
            print("Turn RIGHT onto %s street." % ins[ic+1])
    ic += 2