# Chefs in his Office

def total_working_hours(X, Y):
    return (4 * X) + Y  # 4 days of X hours, 1 day of Y hours

# number of test cases
T = int(input())

# process each test case
for _ in range(T):
    X, Y = map(int, input().split())
    print(total_working_hours(X, Y))