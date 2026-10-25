class Solution:
    def reverse(self, x: int) -> int:
        # Determine the sign
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits using math
        reversed_num = 0
        while x > 0:
            last_digit = x % 10
            reversed_num = reversed_num * 10 + last_digit
            x //= 10
            
        reversed_num *= sign
        
        # Check 32-bit signed integer limits [-2^31, 2^31 - 1]
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
            
        return reversed_num