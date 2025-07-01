class Solution {
public:
    int possibleStringCount(string word) {
        char curr = ' ';
        int count = 0;
        int ans = 1;
        for (const auto& ch : word) {
            if (curr == ' ' || ch != curr) {
                if (count > 0) {
                    ans += count - 1;
                }
                curr = ch;
                count = 1;
            } else {
                count++;
            }
        }
        if (count > 0) {
             ans += count - 1;
        }

        return ans;
    }
};