# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        l=None
        if original is None:
            return None
        if original.val==target.val:
            return cloned
        if original.left is not None:
            l=self.getTargetCopy(original.left, cloned.left, target)
        if l is None and original.right is not None:
            return self.getTargetCopy(original.right, cloned.right, target)
        return l