class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> numsset(nums.begin(), nums.end());
        vector<int> sortednums = vector<int>(numsset.begin(), numsset.end());
        int cur_len = 1;
        int max_len = min(1, (int)nums.size());
        for (size_t i = 1; i < sortednums.size(); ++i) {
            if (sortednums[i]==sortednums[i-1]+1){
                ++cur_len;
                max_len = max(cur_len, max_len);
            }
            else{
                cur_len = 1;
            }
        }
        return max_len;
    }    
};