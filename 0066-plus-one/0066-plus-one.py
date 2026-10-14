class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Iterate from the last element to the first
        for i in range(len(digits) - 1, -1, -1):
            # If the current digit is less than 9, simply add 1 and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If the digit is 9, it becomes 0, and the loop continues to the next digit
            digits[i] = 0
            
        # If the loop finishes without returning, it means all digits were 9 
        # (e.g., [9] becomes [0], so we need to return [1, 0])[cite: 22]
        return [1] + digits