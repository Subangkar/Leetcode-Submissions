# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        s_init = ListNode()
        sum = s_init
        c=0
        
        while l1 is not None or l2 is not None or c>0:
            # sum.next = ListNode()
            s, c= self.addUtil(l1, l2, c)
            
            # sum.val = s
            sum.next = ListNode(val=s)
            
            sum = sum.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return s_init.next
        # return addUtil(l1, l2, ListNode())
    
    def addUtil(self, l1: ListNode, l2: ListNode, c=0): # l3: ListNode,
        # if l1 is None and l2 is None:
            # return l3
        v1 = 0 if l1 is None else l1.val
        v2 = 0 if l2 is None else l2.val
        s=(v1+v2+c)%10
        c=(v1+v2+c)//10
        return s, c
        # l3.next = ListNode(val=s)
        
        # return self.addUtil(l1.next, l2.next, l3.next, c)
        
        