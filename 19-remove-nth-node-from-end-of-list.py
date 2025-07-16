# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nth_prev = None
        nth_last = head
        current = head
        for i in range(n):
            if current:
                current = current.next
            else:
                return head # Less than N nodes in list

        if current:
            while current:
                current = current.next
                nth_prev = nth_last
                nth_last = nth_last.next
            nth_prev.next = nth_last.next
        else:
            head = head.next
        del nth_last
        return head
