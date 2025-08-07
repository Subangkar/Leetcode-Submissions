# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def preUtil(head):
            if not head.left and not head.right:
                # print(head.val, end=' ')
                return head
            
            # print('>', head.val, end=' ')
            second = None
            if head.left:
                ltail = preUtil(head.left)
                ltail.right = head.right
                second = head.left
                tail = ltail
            if head.right:
                if not second:
                    second = head.right
                rtail = preUtil(head.right)
                tail = rtail

            head.left = None
            head.right = second
            # lchild.right = head.right
            return tail
        
        if root:
            preUtil(root)