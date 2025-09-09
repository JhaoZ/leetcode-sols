class Solution {
public:
    int minAbsoluteDifference(vector<int>& nums, int x) {
        if (x == 0) return 0; // same index allowed → 0 immediately
        int ans = INT_MAX;
        std::set<int> seen;

        for (int j = 0; j < (int)nums.size(); ++j) {
            if (j - x >= 0) seen.insert(nums[j - x]);

            if (!seen.empty()) {
                auto it = seen.lower_bound(nums[j]); // <-- key change

                if (it != seen.end()) {
                    ans = std::min(ans, std::abs(*it - nums[j]));
                    if (ans == 0) return 0;
                }
                if (it != seen.begin()) {
                    --it;
                    ans = std::min(ans, std::abs(*it - nums[j]));
                    if (ans == 0) return 0;
                }
            }
        }
        return ans;
    }
};
