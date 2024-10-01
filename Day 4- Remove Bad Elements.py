# Remove Bad Elements

def min_operations(arr, N):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq(num) == 1
    max_freq = max (freq.values())
    return N - max_freq

X = int(input())
for _ in range(X):
    Y = int(input())
    arr = list(map(int, input().split()))
    print(min_operations(arr, Y))