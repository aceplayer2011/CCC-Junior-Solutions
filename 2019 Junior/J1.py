a_cnt = int(input()) * 3 + int(input()) * 2 + int(input())
b_cnt = int(input()) * 3 + int(input()) * 2 + int(input())

if a_cnt>b_cnt:
    print("A")
elif b_cnt>a_cnt:
    print("B")
elif a_cnt == b_cnt:
    print("T")