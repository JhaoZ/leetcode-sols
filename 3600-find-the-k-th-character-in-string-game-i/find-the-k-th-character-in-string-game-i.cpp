class Solution {
public:
    char kthCharacter(int k) {
        string s = "a";
        std::unordered_map<char, char> next;
        for (char a = 'a'; a < 'z'; ++a) {
            next[a] = (char)(a + 1);
        }
        next['z'] = 'a';

        while (s.size() < k) {
            string new_str = "";
            for (const auto& ch : s) {
                new_str += next[ch];
            }
            s += new_str;
        }
        return s[k - 1];
    }
};