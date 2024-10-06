# Plus One

def plusOne(digits):
    # Make a copy of the original list to avoid modifying it
    digits = digits.copy()
    
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        
        digits[i] = 0

    return [1] + digits

digits1 = [1, 2, 9]
print(plusOne(digits1))  # Output: [1, 3, 0]

digits2 = [9, 9, 9]
print(plusOne(digits2))  # Output: [1, 0, 0, 0]