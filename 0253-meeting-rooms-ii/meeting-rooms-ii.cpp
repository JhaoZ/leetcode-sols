class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        std::unordered_map<int, int> prefix;
        std::unordered_set<int> keys;
        for (auto& vec : intervals) {
            prefix[vec[0]] += 1;
            keys.insert(vec[0]);
            prefix[vec[1]] -= 1;
            keys.insert(vec[1]);
        }
        int csum = 0;
        int ans = 0;
        std::vector<int> keyset;
        for (const auto& k : keys) {
            keyset.push_back(k);
        }
        sort(keyset.begin(), keyset.end());
        for (auto& k : keyset) {
            csum += prefix[k];
            ans = std::max(ans, csum);
        }
        return ans;
    }
};