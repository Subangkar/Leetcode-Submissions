class Solution {

    int bsearch(const vector<int>& vec, int left, int right, int target) {
        int mid = left + (right - left) / 2;
        
        if (vec[mid] == target) {
            return mid;
        }
        else if(left == right){
            return vec[left]>target ? left: left+1;
        }
        else if (vec[mid] > target) {
            return bsearch(vec, left, max(mid - 1, left), target);
        }
        else {
            return bsearch(vec, min(mid + 1, right), right, target);
        }
    }


public:
    int searchInsert(vector<int>& nums, int target) {
        return bsearch(nums, 0, nums.size() - 1, target);
    }
};