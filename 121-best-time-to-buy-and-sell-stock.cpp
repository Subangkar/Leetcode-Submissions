class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n < 2) return 0;
        int mins[n];
        mins[0] = 100001;
        mins[1] = prices[0];
        
        for(int i = 2; i<n; ++i){
            mins[i] = min(prices[i-1], mins[i-1]);
        }
        int maxP = 0; 
        for(int i = 1; i<n; ++i){
            maxP = max(maxP, prices[i]-mins[i]);
        }
        return maxP;
    }
};