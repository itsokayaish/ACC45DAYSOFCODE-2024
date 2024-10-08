# Mask Policy

def min_masks_required(N, A):
    half_population = (N + 1) // 2
    if A >= half_population:
        return 0
    else:
        return half_population - A

T = int(input("Enter number of test cases: "))
for _ in range(T):
    N = int(input("Enter population size: "))  # population size
    A = int(input("Enter number of people already vaccinated: "))  # number of people already
    # vaccinated
    print(min_masks_required(N, A))  # print the minimum number of masks required