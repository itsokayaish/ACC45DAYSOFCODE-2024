# Ratio by 2

def min_operations_to_ratio(T, test_cases):
    for i in range(T):
        X, Y= test_cases[i]
        moves = 0
        while x < 2 * Y and Y < 2 * X:
            if X > Y:
                X += 1
            else:
                Y += 1
                moves += 1
        print(moves)

T = int(input())
test_cases = []
for _ in range(T):
    X, Y = map(int, input().split())
    test_cases.append((X, Y))

min_operations_to_ratio(T, test_cases)