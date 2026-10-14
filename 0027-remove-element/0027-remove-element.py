class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # Pointer for the position of the next valid element
        
        for i in range(len(nums)):
            # If the current element is not the value to remove
            if nums[i] != val:
                nums[k] = nums[i]  # Place it at the k-th position
                k += 1             # Increment the count of valid elements
                
        # k now represents the number of elements not equal to val[cite: 13]
        return k