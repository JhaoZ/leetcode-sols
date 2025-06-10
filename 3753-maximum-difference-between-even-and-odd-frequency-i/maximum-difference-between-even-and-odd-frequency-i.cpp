class Solution {
public:
    int maxDifference(string s) {
        int freq[26];
        for (int i = 0; i < 26; ++i) freq[i] = 0;
        int max_odd = 0;
        int max_even = 0;
        int min_odd = INT_MAX;
        int min_even = INT_MAX;
        for (int i = 0; i < s.size(); ++i) {
            freq[s[i] - 'a']++;
        }

        for (char i = 'a'; i <= 'z'; ++i) {
            if (freq[i - 'a'] == 0) continue;
            if (freq[i - 'a'] % 2 == 0) {
                max_even = max(max_even, freq[i - 'a']);
                min_even = min(min_even, freq[i - 'a']);
            } else {
                max_odd = max(max_odd, freq[i - 'a']);
                min_odd = min(min_odd, freq[i - 'a']);
            }
        }
       
        return (max_odd - min_even);
        
    }
};