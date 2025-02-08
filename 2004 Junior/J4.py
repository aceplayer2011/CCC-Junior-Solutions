import sys

keyword = sys.stdin.readline().strip()
message = sys.stdin.readline().strip()

message = "".join([c for c in message if c.isalpha()])

encoded = []
keyword_length = len(keyword)

for i, char in enumerate(message):
    shift = ord(keyword[i % keyword_length]) - ord('A')
    new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    encoded.append(new_char)

print("".join(encoded))