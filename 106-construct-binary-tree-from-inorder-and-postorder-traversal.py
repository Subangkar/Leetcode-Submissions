# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        inord_idx = {v:i for i,v in enumerate(inorder)}

        self.post_idx = len(postorder)-1
        def buildUtil(l, r):
            if l>r:
                return None

            root = TreeNode()
            root.val = postorder[self.post_idx]
            mid = inord_idx[root.val]
            
            self.post_idx -= 1

            root.right = buildUtil(mid+1, r)
            root.left = buildUtil(l, mid-1)
            
            return root

        return buildUtil(0, len(postorder)-1)

            

                