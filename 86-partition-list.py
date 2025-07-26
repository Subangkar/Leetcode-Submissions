# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_list_head = less_list = ListNode()
        gret_list_head = gret_list = ListNode()

        while head:
            if head.val < x:
                less_list.next = head
                less_list = less_list.next
            else:
                gret_list.next = head
                gret_list = gret_list.next
            head = head.next
        gret_list.next = None
        less_list.next = gret_list_head.next
        return less_list_head.next
        