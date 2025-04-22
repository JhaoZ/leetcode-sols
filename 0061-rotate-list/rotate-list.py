# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        size = 1
        curr = head
        while curr.next != None:
            size += 1
            curr = curr.next
        curr.next = head

        run = ((size - (k % size)) - 1 + size) % size
        prev = head
        curr = head.next
        for i in range(0, run):
            prev = curr
            curr = curr.next
        
        prev.next = None
        return curr

        