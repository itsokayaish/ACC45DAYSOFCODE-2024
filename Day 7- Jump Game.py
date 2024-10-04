# Jump Game

def max_people_in_room(N, X, A):
    current_people = X
    max_people = X
    for i in range(N):
        current_people += A[i]
        max_people = max(max_people, current_people)
    return max_people
T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list( map(int, input().split()))
print(max_people_in_room(N, X, A))