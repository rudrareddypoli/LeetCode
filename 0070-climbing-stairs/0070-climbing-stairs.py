class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # Base cases: 1 way for 1 step, 2 ways for 2 steps
        prev2, prev1 = 1, 2
        
        # Each step can be reached from (i - 1) or (i - 2)[cite: 25]
        for _ in range(3, n + 1):
            prev2, prev1 = prev1, prev2 + prev1
            
        return prev1