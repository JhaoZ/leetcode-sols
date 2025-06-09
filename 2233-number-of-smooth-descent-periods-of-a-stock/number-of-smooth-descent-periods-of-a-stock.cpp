class Solution {
public:
    long long getDescentPeriods(vector<int>& prices) {
        int start = 0;
        long long ans = 0;
        for (int i = 0; i < prices.size(); ++i) {
            if (i == 0) {
                ans++;
            } else {
                if (prices[i - 1] - 1 == prices[i]) {
                    ans += i - start + 1;
                } else {
                    ans++;
                    start = i;
                }
            }
        }
        return ans;
    
    }
};