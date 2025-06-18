class Solution {
public:
    int maxSumDistinctTriplet(vector<int>& x, vector<int>& y) {
        unordered_map<int, int> dict;
        for (int i = 0; i < x.size(); ++i) {
            dict.at(x[i]) = max(dict[x[i]], y[i]);
        }
        vector<int> temp;
        for (const auto& [k, v] : dict) {
            temp.push_back(v);
        }
        sort(temp.begin(), temp.end(), greater<int>());

        if (temp.size() < 3) return -1;

        return temp[0] + temp[1] + temp[2];
    }
};