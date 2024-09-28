# TWO SUM PROBLEM
# Given an array of integers nums and an integr target, return indices of the two numbers such that they add up to the target.

def two_sum(nums, target):

    # iterate over the indices of the nums array
    for i in range(len(nums)):

        # iterate over the indices of the nums array starting from i+1
        for k in range(i+1, len(nums)):

            # check if the sum of the numbers at indices i and k is equal to the target
            if nums[i] + nums[k] == target:
                return [i, k]
    return []  # return empty list if no solution is found

# define a sample nums array and targte values
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  

# Output: [0, 1]