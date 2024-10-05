# Pseudo Sorted Array

def is_pseudo_sorted(N, A):
    # initialize swap count to 0
    swap_count = 0

    for i in range(N - 1):
        if A[i] > A[i+1]:
            swap_count += 1
            if swap_count > 1:
                return "NO"

    # return the result after processing all elements in the list A
    return "YES" if swap_count <= 1 else "NO"

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(is_pseudo_sorted(N,A))