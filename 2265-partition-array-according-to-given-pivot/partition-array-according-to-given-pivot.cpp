class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        int less_cnt = 0;
        int piv_cnt = 0;
        int great_cnt = 0;
        for (const auto& num : nums) {
            if (num < pivot) {
                less_cnt++;
            } else if (num > pivot) {
                great_cnt++;
            } else {
                piv_cnt++;
            }
        }
        vector<int> ans(nums.size(), 0);
        for (int i = 0; i < piv_cnt; ++i) {
            ans[less_cnt + i] = pivot;
        }
        int ptr_less = 0;
        int ptr_more = less_cnt + piv_cnt;
        for (const auto& num : nums) {
            if (num < pivot) {
                ans[ptr_less] = num;
                ptr_less++;
            } else if (num > pivot) {
                ans[ptr_more] = num;
                ptr_more++;
            }
        }
        
        return ans;
    }
};