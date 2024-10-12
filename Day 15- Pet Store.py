# Pet Store

def can_split_animals(animal_types):
    """
    Checks if the given animal types can be split into pairs.

    Args:
        animal_types (list): A list of animal types.

    Returns:
        str: "Yes" if the animals can be split into pairs, "No" otherwise.
    """
    freq = {}
    for animal in animal_types:
        freq[animal] = freq.get(animal, 0) + 1
    
    for count in freq.values():
        if count % 2 != 0:
            return "No"
    return "Yes"

def main():
    """
    Reads input from the user and checks if the given animal types can be split into pairs.
    """
    T = int(input())
    for _ in range(T):
        N = int(input())
        animal_types = list(map(int, input().split()))
        result = can_split_animals(animal_types)
        print(result)

if __name__ == "__main__":
    main()