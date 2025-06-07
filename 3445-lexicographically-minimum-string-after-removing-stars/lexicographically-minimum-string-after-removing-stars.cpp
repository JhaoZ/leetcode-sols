class Solution {
public:
    string clearStars(string s) {
        std::unordered_map<char, std::set<int>> maps;
        vector<int> stars;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] != '*') {
                maps[s[i]].insert(i);
            } else {
                stars.push_back(i);
            }
        }

        for (const auto& pos : stars) {
            for (char i = 'a'; i <= 'z'; ++i) {
                auto it = maps[i].upper_bound(pos);
                if (it != maps[i].begin()) {
                    it--;
                    maps[i].erase(it);
                    break;
                }
            }
        }

        string ans = "";
        for (int i = 0; i < s.size(); ++i) {
            for (char j = 'a'; j <= 'z'; ++j) {
                if (maps[j].count(i)) {
                    ans += j;
                    break;
                }
            }
        }
        return ans;

        
    }
};