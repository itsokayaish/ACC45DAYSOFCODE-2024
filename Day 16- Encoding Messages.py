# Encoding Messages

def encode_message(s):
    n = len(s)
    s = list(s)
    for i in range(0, n - 1, 2):
        s[i], s[i + 1] = s[i + 1], s[i]
    s = ''.join(s)
    encoded_message = []
    for char in s:
        new_char = chr(219 - ord(char))
        encoded_message.append(new_char)
    return ''.join(encoded_message)

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(encode_message(s))