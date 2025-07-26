# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        b4head = ListNode(next=head) # to handle case where whole list is reversed
        curhead = b4head
        i = 0

        leftPrev = None
        while i<left:
            leftPrev = curhead
            curhead = curhead.next
            i += 1

        lefthead = curhead # left of sublist
        rightTail = lefthead # right of sublist
        while i<=right:
            nxt = curhead.next
            curhead.next = rightTail
            rightTail = curhead

            curhead = nxt
            i += 1

        lefthead.next = curhead
        leftPrev.next = rightTail
        
        return b4head.next            
        