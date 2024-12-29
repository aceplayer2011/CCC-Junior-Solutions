K = int(input())
letters = input()
for idx, letter in enumerate(letters):
    S = (idx+1)*3+K
    x = ord(letter)-S
    if x < ord('A'):
        x += 26
    print(chr(x), end='')
print()