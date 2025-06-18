class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        int n = nums.size() / 3;
        for (int i = 0; i < n; ++i) {
            if (nums[3 * i + 2] - nums[3 * i] <= k) {
                ans.push_back({nums[3*i], nums[3*i+1], nums[3*i+2]});
            } else {
                return vector<vector<int>>();
            }
        }
        return ans;
    }
};