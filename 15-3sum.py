class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        orig_list = nums
        sorted_list = sorted(orig_list)

        sublists = []

        for i in range(0, len(sorted_list) - 1):
            # if i's value has been used before shift i to new value
            if i>0 and sorted_list[i] == sorted_list[i - 1]:
                continue
            j = i + 1
            k = len(sorted_list) - 1
            while j<k:
                total = sorted_list[i] + sorted_list[j] + sorted_list[k]
                if total == 0:
                    sublists.append([sorted_list[i], sorted_list[j], sorted_list[k]])
                    j += 1
                    # shift j to rightmost of duplicates
                    while j<k and sorted_list[j] == sorted_list[j - 1]:
                        j += 1
                        continue
                else:
                    if total>0:
                        k -= 1
                    else:
                        j += 1

        return sublists
