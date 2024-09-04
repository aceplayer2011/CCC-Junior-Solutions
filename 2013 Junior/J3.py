firstnum = int(input())

def distinct(num):
    digits = str(num)
    return len(digits) == len(set(digits))
def next_distinct(num):
    while True:
        num += 1
        if distinct(num):
            return num
    return None

next_number = next_distinct(firstnum)
if next_number is not None:
    print(f"{next_number}")