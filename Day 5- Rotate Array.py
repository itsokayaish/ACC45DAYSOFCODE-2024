# Rotate Array

def rotate_array(num, k):

    # if k is greater than the length of nums, take k modulus  the length of nums
    k = k % len(nums)

    # slice the array and rotate
    nums[:] = nums[-k:] + nums[:-k]

nums = [10, 20, 30, 40, 50, 60, 70]
k = 2
rotate_array(nums, k)
print(nums)

# output will be [60, 70, 10, 20, 30, 40, 50]