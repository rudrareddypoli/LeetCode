class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_bound(find_first: bool) -> int:
            left, right = 0, len(nums) - 1
            index = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    index = mid
                    if find_first:
                        right = mid - 1  # Keep searching left for first appearance
                    else:
                        left = mid + 1   # Keep searching right for last appearance
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return index

        start = find_bound(find_first=True)
        end = find_bound(find_first=False)
        
        return [start, end]