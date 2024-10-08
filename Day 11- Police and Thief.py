# Police and Thief

def min_time_to_catch (X, Y):
    if X == Y:
        return 0
    else:
        distance = abs(X - Y)
        return (distance + 1) // 2

T = int(input("Enter number of test cases: "))

for _ in range (T):
    X, Y = map(int, input().split())
    print(min_time_to_catch(X, Y))