# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeSortedList(self, l1: ListNode, l2: ListNode):
        dummy = ListNode()
        head = dummy
        while l1 and l2:
            if l1.val<=l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        pmid = head
        slow = head
        fast = head
        while fast and fast.next:
            pmid = slow
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        pmid.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.mergeSortedList(left, right)