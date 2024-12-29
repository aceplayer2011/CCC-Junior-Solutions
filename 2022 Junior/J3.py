def letter(ch):
    return ch >= 'A' and ch <= 'T'
def digit(ch):
    return ch >='0' and ch<='9'

s = input()
prev = ' '
updated = ''
for curr in s:
    if letter(curr) and digit(prev):
        updated += '\n'
    updated += curr
    prev = curr
updated = updated.replace("+", " tighten ").replace("-", " loosen ")
print(updated)