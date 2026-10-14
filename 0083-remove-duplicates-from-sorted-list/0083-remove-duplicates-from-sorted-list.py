# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        current = head
        
        # Traverse the list while the current node and next node exist
        while current and current.next:
            # If the current value matches the next node's value, bypass the duplicate
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                # Otherwise, move forward to the next distinct node
                current = current.next
                
        return head