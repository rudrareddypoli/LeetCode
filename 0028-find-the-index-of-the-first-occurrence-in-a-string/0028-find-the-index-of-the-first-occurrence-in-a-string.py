class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)
        
        # Iterate through the haystack up to the point where the remaining characters 
        # are at least the length of the needle
        for i in range(h_len - n_len + 1):
            # Check if the current slice matches the needle
            if haystack[i : i + n_len] == needle:
                return i
                
        # If the loop finishes without returning, the needle is not in the haystack
        return -1