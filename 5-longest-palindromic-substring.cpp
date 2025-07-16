#include <bits/stdc++.h>
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        int dp_len[n][n];
        for(int r = 0; r < n; ++r)
            for(int c = 0; c < n; ++c)
                dp_len[r][c] = 0;
        for(int r = 0; r < n; ++r)
            dp_len[r][r] = 1;

        int max_len = 1;
        int max_r = 0;
        int max_c = 0;
        for (int l = 1; l < n; ++l){
            for (int r = 0; r < n-l; ++r){
                int c = r + l;
                if (s[r] == s[c] && ((c - r < 2) || dp_len[r + 1][c - 1] > 0)){
                    dp_len[r][c] = 2 + dp_len[r + 1][c - 1];
                    if (dp_len[r][c] > max_len){
                        max_len = dp_len[r][c];
                        max_r = r;
                        max_c = c;
                    }
                }
            }
        }
        return s.substr(max_r, max_len);
    }
};