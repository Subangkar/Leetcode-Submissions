# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rbst(self, nums: List[int], l: int , r: int) -> Optional[TreeNode]:
        if l>r:
            return None

        m = l + (r-l)//2
        return TreeNode(val=nums[m],    left=self.rbst(nums, l, m-1),
                                        right=self.rbst(nums, m+1, r))

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.rbst(nums, 0, len(nums)-1)