# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_list = []
        count = 0
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_list.append(node.val)
            if len(sorted_list)>=k:
                return
            inorder(node.right)
        inorder(root)
        return sorted_list[k-1]