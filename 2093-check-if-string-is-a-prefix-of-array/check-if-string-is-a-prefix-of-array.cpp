class Solution {
public:
    bool isPrefixString(string s, vector<string>& words) {
        string total = "";
        for (const auto& st : words) {
            total += st;
        }

        for (auto it = words.rbegin(); it != words.rend(); it++) {
            if (total.size() <= s.size() && total == s) {
                return true;
            } 
            total = total.substr(0, total.size() - (*it).size());
        }
        return false;
    }
};