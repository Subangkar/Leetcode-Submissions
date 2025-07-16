# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        current = head
        tail = None
        while current:
            tail = current
            current = current.next
            n += 1
        if n==0 or k%n==0:
            return head

        k = k%n
        # find the new starting node and its previous one in original list
        kth_prev = None
        kth_last = head
        for i in range(n-k):
            kth_prev = kth_last
            kth_last = kth_last.next
        
        old_head = head
        head = kth_last
        tail.next = old_head
        kth_prev.next = None 
        return head
        