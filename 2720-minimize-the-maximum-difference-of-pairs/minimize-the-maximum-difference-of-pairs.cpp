class Solution {
public:

    int possible(int threshold, vector<int>& nums) {
        int cnt = 0;
        for (int i = 0; i < nums.size() - 1; ++i) {
            if (abs(nums[i] - nums[i + 1]) <= threshold) {
                cnt++;
                i++;
            }
        }
        return cnt;
    }

    int minimizeMax(vector<int>& nums, int p) {
        sort(nums.begin(), nums.end());
        int left = 0;
        int right = nums[nums.size() - 1] - nums[0];
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            if (possible(mid, nums) >= p) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};