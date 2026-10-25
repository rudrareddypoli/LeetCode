class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        path = []

        def backtrack(start: int):
            # Base case: we have chosen k numbers
            if len(path) == k:
                result.append(path.copy())
                return

            # Try adding numbers from 'start' up to 'n'
            for num in range(start, n + 1):
                path.append(num)       # Choose
                backtrack(num + 1)     # Explore next numbers
                path.pop()             # Un-choose (backtrack)

        backtrack(1)
        return result