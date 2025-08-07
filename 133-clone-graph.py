"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        ht = {}
        def dfs(node_):        
            for nbr in node_.neighbors:
                explore = False
                if nbr.val not in ht:
                    ht[nbr.val] = Node(nbr.val)
                    explore = True
                ht[node_.val].neighbors.append(ht[nbr.val])
                if explore:
                    dfs(nbr)

        ht[node.val] = Node(node.val)
        dfs(node)

        # print(ht)
        # for k,v in ht.items():
        #     print(k, '->', v.neighbors)
        return ht[1]