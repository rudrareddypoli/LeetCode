class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        
        # 1. Define the 4 boundaries
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        
        # 2. Keep going until boundaries cross each other
        while top <= bottom and left <= right:
            
            # Move RIGHT: along the current top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1  # Top row is done, push the boundary down
            
            # Move DOWN: along the current right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1  # Right column is done, push the boundary left
            
            # Move LEFT: along the current bottom row
            # (Check top <= bottom so we don't re-read an already processed row)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1  # Bottom row is done, push the boundary up
                
            # Move UP: along the current left column
            # (Check left <= right so we don't re-read an already processed column)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1  # Left column is done, push the boundary right
                
        return result