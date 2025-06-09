class Solution {
public:
    long long minOperationsToMakeMedianK(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int mid_idx = (nums.size())/2;
        int curr_med = nums[mid_idx];
        long long ops = 0;
        if (curr_med == k) {
            return ops;
        } else if (curr_med > k) {
            for (int i = mid_idx; i >= 0; --i) {
                ops += max(0, nums[i] - k);
            }
        } else {
            for (int i = mid_idx; i < nums.size(); ++i) {
                ops += max(0, k - nums[i]);
            }
        }
        return ops;

    }
};