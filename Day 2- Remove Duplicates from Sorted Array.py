# Remove Duplicates from Sorted Array

def remove_duplicates (nums):
    # if the array is empty , return 0

    if not nums:
        return 0
    
    unique_index = 0

    for i in range (1, len(nums)):
        if nums [i] != nums [unique_index]:

            unique_index +=1
            nums [unique_index] = nums[i]

    return unique_index + 1

nums = [1, 1, 2, 2, 3, 3, 4, 4, 5]
k = remove_duplicates (nums)

print(f"Number of unique elements: {k}")
print(f"Array after removing duplicates: {nums[:k]}")