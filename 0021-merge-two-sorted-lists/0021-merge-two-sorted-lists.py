# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # Create a dummy node to act as the starting point of the merged list
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists while neither is empty
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        # If any elements remain in either list, append them to the end
        # This handles cases where one list is longer or examples like list1 = [], list2 = [0][cite: 10]
        current.next = list1 if list1 else list2
        
        # The head of the merged list is the node after the dummy
        return dummy.next