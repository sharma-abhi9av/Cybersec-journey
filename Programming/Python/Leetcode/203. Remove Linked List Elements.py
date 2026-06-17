"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
```
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
```
Example 2:
```
Input: head = [], val = 1
Output: []
```
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy =ListNode(0)
        dummy.next = head 
        current = dummy 
        while current.next != None :
            if current.next.val == val :
                current.next = current.next.next
            else : 
                current = current.next
        return dummy.next
