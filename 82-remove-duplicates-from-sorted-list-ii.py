# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        b4head = ListNode(next=head)
        prevleft = b4head
        left = head
        right = head.next
        while True:
            count=0
            while right and right.val == left.val:
                right = right.next
                count += 1
            if count==0:
                prevleft.next = left
                prevleft = prevleft.next
                # print(prevleft.val)
            if not right:
                break
            # print(left.val)
            left = right
            right = right.next
        prevleft.next = None
        return b4head.next
        