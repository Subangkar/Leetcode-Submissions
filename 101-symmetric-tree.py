# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def symutil(self, lt, rt) -> bool:
        if not lt and not rt:
            return True
        if lt and rt and lt.val==rt.val:
            return self.symutil(lt.left, rt.right) and self.symutil(lt.right, rt.left)
        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.symutil(root.left, root.right)