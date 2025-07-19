# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3_l = []
        
        c = 0
        while l1 or l2:
            s = c
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            c = s//10
            s = s%10
            l3_l.append(s)

        if c>0:
            l3_l.append(c)

        p = l3 = ListNode(val=l3_l[0])
        for x in l3_l[1:]:
            p.next = ListNode(val=x)
            p = p.next
        return l3
        