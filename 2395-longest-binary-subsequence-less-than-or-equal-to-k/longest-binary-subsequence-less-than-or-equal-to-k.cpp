class Solution {
public:
    int longestSubsequence(string s, int k) {
        long long val = 0;          // current numeric value
        long long pow2 = 1;         // weight of the next bit (LSB first)
        int ones   = 0;             // chosen '1' bits

        // pick bits from least-significant side (right → left)
        for (int i = (int)s.size() - 1; i >= 0 && pow2 <= k; --i) {
            if (s[i] == '1') {
                if (val + pow2 <= k) {   // safe to take this '1'
                    val  += pow2;
                    ++ones;
                }
            }
            pow2 <<= 1;                  // move to the next more-significant bit
        }

        int zeros = count(begin(s), end(s), '0');   // zeros never change the value
        return zeros + ones;
    }
};
