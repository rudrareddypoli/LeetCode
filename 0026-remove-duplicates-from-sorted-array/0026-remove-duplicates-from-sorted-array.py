class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Since the array is guaranteed to have at least length 1 based on constraints,
        # the first element is always unique.
        insert_index = 1
        
        # Iterate from the second element to the end
        for i in range(1, len(nums)):
            # If the current element is different from the previous one, it's a new unique element
            if nums[i] != nums[i - 1]:
                nums[insert_index] = nums[i]
                insert_index += 1
                
        # The insert_index now represents the number of unique elements (k)
        return insert_index