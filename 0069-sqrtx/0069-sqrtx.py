class Solution:
    def mySqrt(self, x: int) -> int:
        # Base cases for 0 and 1
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
                
        # When left > right, right holds the integer rounded down
        return right