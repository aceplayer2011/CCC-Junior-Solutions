def print_calendar(d, n):
    print("Sun", "Mon", "Tue", "Wed", "Thr", "Fri", "Sat")
    date = 1
    for i in range(d + n - 2):
        if i < d - 1:
            print(" " * 3, end=" ")
        else:
            if i % 7 == 6:
                print(f'{date:>3}')
                date += 1
            else:
                print(f'{date:>3}', end=" ")
                date += 1
    print(f'{date:>3}')

if __name__ == "__main__":
    d, n = map(int, input().split())
    print_calendar(d, n)