"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldhead = head
        newhead = Node(x=0)
        old_to_new = {None:None}

        curhead = newhead
        while head:
            curhead.next = Node(x=head.val)
            old_to_new[head] = curhead.next
            curhead = curhead.next
            head = head.next        
        newhead = newhead.next

        curhead = newhead
        head = oldhead
        while head:
            curhead.random = old_to_new[head.random]
            curhead = curhead.next
            head = head.next

        return newhead
        