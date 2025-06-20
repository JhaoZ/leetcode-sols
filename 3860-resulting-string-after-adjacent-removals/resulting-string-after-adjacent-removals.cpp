class Solution {
public:

    bool removable(char a, char b) {
        return (a == 'a' && b =='z') || (a == 'z' && b == 'a') || (abs(a - b) == 1);
    }

    string resultingString(string s) {
        vector<char> stack;
        for (const auto& ch : s) {
            if (stack.empty()) {
                stack.push_back(ch);
            } else {
                if (removable(stack[stack.size() - 1], ch)) {
                    stack.pop_back();
                } else {
                    stack.push_back(ch);
                }
            }
        }
        string ans = "";
        for (const auto& ch : stack) {
            ans += ch;
        }
        return ans;
    }
};