class Solution {
public:
    int maximizeGreatness(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int ans = 0;
        vector<int> temp(nums);
        int ptr = 0;
        for (const auto& val : nums) {
            while (ptr < temp.size() && nums[ptr] <= val) {
                ptr++;
            }
            if (ptr < temp.size() && nums[ptr] > val) {
                ans++;
                ptr++;
            }
        }
        return ans;
    }
};