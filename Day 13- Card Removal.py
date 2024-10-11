# Card Removal

def min_moves_to_same(T, test_cases):
    for i in range(T):
        N = test_cases[i][0]
        freq = {}

        for card in cards:
            if card in freq:
                freq[card] += 1
            else:
                freq[card] = 1

        max_freq = max(freq.values())
        print(N - max_freq)

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    cards = list(map(int, input(.split())))
    test_casesappend((N, cards))
min_moves_to_same(T, test_cases)