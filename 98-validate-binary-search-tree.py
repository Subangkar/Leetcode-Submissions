# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isBstUtil(node, min_so_far, max_so_far):
            if not node:
                return True
            if not min_so_far<node.val<max_so_far:
                return False
            return isBstUtil(node.left, min_so_far, node.val) and isBstUtil(node.right, node.val, max_so_far)

        INT_MIN_64 = -(2**63)         # -9223372036854775808
        INT_MAX_64 = 2**63 - 1        # 9223372036854775807
        return isBstUtil(root, INT_MIN_64, INT_MAX_64)
        