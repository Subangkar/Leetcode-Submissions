class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        first_k_elems = nums[:len(nums)-k] 
        last_k_elems = nums[len(nums)-k:]
        nums[0:k] = last_k_elems
        nums[k:] = first_k_elems
        
        

        