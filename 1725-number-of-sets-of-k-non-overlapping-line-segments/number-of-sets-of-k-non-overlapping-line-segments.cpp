class Solution {
public:
    static constexpr int MOD = 1e9 + 7;
    int n, k;

    int dp(int idx, int left, bool opened, vector<vector<vector<int>>>& memo) {
        if (idx == n)
            return (left == 0 && !opened) ? 1 : 0;

        if (memo[idx][left][opened] != -1)
            return memo[idx][left][opened];

        long long ans = 0;

        if (opened) {
            // 1. Extend
            ans = (ans + dp(idx + 1, left, true, memo)) % MOD;
            // 2. Close
            if (left > 0)
                ans = (ans + dp(idx + 1, left - 1, false, memo)) % MOD;
            // 3. Close and open another
            if (left >= 2)
                ans = (ans + dp(idx + 1, left - 1, true, memo)) % MOD;
        } else {
            // 1. Skip
            ans = (ans + dp(idx + 1, left, false, memo)) % MOD;
            // 2. Open
            if (left > 0)
                ans = (ans + dp(idx + 1, left, true, memo)) % MOD;
        }

        return memo[idx][left][opened] = ans;
    }

    int numberOfSets(int n_, int k_) {
        n = n_;
        k = k_;
        // Dimensions: idx (0..n), left (0..k), opened (0/1)
        vector<vector<vector<int>>> memo(n + 1, vector<vector<int>>(k + 1, vector<int>(2, -1)));
        return dp(0, k, false, memo);
    }
};
