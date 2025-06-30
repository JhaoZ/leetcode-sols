class Solution {
public:
    int findLHS(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        unordered_map<int, int> freq;
        for (const auto& n : nums) {
            freq[n]++;
        }

        int ans = 0;
        for (const auto& [k, v] : freq) {
            if (freq.find(k + 1) != freq.end()) {
                ans = max(ans, v + freq[k + 1]);
            }
        }
        return ans;

    }
};