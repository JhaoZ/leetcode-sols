class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        vector<int> j_vec;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums.at(i) == key) j_vec.push_back(i);
        }

        vector<int> ans;
        for (int i = 0; i < nums.size(); ++i) {
            for (const auto& pos : j_vec) {
                if (abs(pos - i) <= k) {
                    ans.push_back(i);
                    break;
                }
            }
        }
        return ans;
    }
};