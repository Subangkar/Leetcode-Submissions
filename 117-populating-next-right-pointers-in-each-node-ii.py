"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q_bfs = deque()
        q_bfs.append(root)
        while q_bfs:
            level_len = len(q_bfs)
            for i in range(level_len):
                node = q_bfs.popleft()                
                if i != (level_len-1):
                    node.next = q_bfs[0]
                if node.left:
                    q_bfs.append(node.left)
                if node.right:
                    q_bfs.append(node.right)
        return root
            

        