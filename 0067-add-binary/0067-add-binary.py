class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        # Continue as long as there are digits left in 'a' or 'b', or a carry remains
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # The bit to add to the result is the remainder of total / 2
            res.append(str(total % 2))
            # The new carry is the quotient of total / 2
            carry = total // 2
            
        # The result was built backwards, so reverse it before joining
        return "".join(res[::-1])