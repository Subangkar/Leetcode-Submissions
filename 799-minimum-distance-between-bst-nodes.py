# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        sorted_list = []
        prev = 100001
        def inorder(node):
            if not node:
                return      
            inorder(node.left)
            sorted_list.append(node.val)
            inorder(node.right)
        inorder(root)
        mindiff = (sorted_list[1]-sorted_list[0])
        for i in range(1, len(sorted_list)):
            mindiff = min(mindiff, (sorted_list[i]-sorted_list[i-1]))
        return mindiff        