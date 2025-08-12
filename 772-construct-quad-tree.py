"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def buildUtil(s, t, n):
            # print('>', s, t, n)
            if n==1:
                # print(s,t)
                return Node(grid[s][t], 1, None, None, None, None)
            tleft = buildUtil(s, t, n//2)
            tRigt = buildUtil(s, t+n//2, n//2)
            bleft = buildUtil(s+n//2, t, n//2)
            bRigt = buildUtil(s+n//2, t+n//2, n//2)
            if (tleft.val+tRigt.val+bleft.val+bRigt.val) in (0,4) and (tleft.isLeaf+tRigt.isLeaf+bleft.isLeaf+bRigt.isLeaf)==4:
                # print('leaf>', s, t, n)
                return Node(tleft.val, 1, None, None, None, None)
            else:
                # print('non-leaf>', s, t, n)
                return Node(0, 0, tleft, tRigt, bleft, bRigt)
            
        return buildUtil(0, 0, len(grid))
        