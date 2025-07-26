# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lca(node):
            if not node:
                return None
            ret_l = lca(node.left)
            ret_r = lca(node.right)
            # print(node.val, '[', ret_l, ',', ret_r, ']')
            if node.val==p.val or node.val==q.val:
                return node
            if ret_l and ret_r:
                return node
            if ret_l:
                return ret_l
            if ret_r:
                return ret_r

        return lca(root)
        