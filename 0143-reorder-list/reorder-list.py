# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        


        fast = head
        slow = head
        while fast != None:
            fast = fast.next
            if fast and fast.next:
                fast = fast.next
                slow = slow.next
        
        # reverse
        next_head = slow.next
        slow.next = None

        curr = next_head
        prev = None
        
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            

        p1 = head
        p2 = prev

        while p1 != None and p2 != None:
            temp = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp
            p2 = temp2
            p1 = p1.next
            if p1:
                p1 = p1.next
            
        return