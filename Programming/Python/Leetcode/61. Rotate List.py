"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
```
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
```
Example 2:
```
Input: head = [0,1,2], k = 4
Output: [2,0,1]
```
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        k = k % length
        if k == 0:
            return head
        fast = head 
        slow = head
        count = 0
        while fast.next:
            
            if count < k:
                fast = fast.next
                count +=1 
            else:
                slow = slow.next
                fast = fast.next
        new_head = slow.next 
        fast.next = head 
        slow.next = None 
        return new_head
