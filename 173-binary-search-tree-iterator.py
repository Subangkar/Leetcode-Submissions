# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        leftmost = root;
        while leftmost:            
            self.stack.append(leftmost)
            leftmost = leftmost.left
        

    def next(self) -> int:
        top = self.stack.pop()
        leftmost = top.right
        while leftmost:
            self.stack.append(leftmost)
            leftmost=leftmost.left
        return top.val
        
        

    def hasNext(self) -> bool:
        if not self.stack:
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()