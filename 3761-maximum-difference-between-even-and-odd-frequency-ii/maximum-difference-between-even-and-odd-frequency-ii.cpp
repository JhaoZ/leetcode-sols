#include <bits/stdc++.h>
using namespace std;

class Solution {
    /* bit-1 : parity of oddChar , bit-0 : parity of evenChar */
    int status(int oddCnt, int evenCnt) { return ((oddCnt & 1) << 1) | (evenCnt & 1); }

    /* maximum  (oddCnt – evenCnt)  for substrings ≥ k
       where oddChar has odd freq and evenChar has *positive* even freq            */
    int maxDiff(char oddChar, char evenChar, const string& s, int k) {
        const int n = s.size();
        vector<int> best(4, INT_MAX);                 // min(prefixOdd – prefixEven) per status
        int odd = 0, even = 0;                        // prefix counts up to “right”
        int prefOdd = 0, prefEven = 0;                // prefix counts up to “left”
        int left = -1;                                // prefix ends at index left
        int ans  = INT_MIN;

        for (int right = 0; right < n; ++right) {
            if (s[right] == oddChar)  ++odd;
            if (s[right] == evenChar) ++even;

            /* push prefixes while:  window ≥ k  AND  evenFreq(window) ≥ 2 (positive even) */
            while (right - left >= k && even - prefEven >= 2) {
                int st = status(prefOdd, prefEven);
                best[st] = min(best[st], prefOdd - prefEven);

                ++left;                               // advance prefix end
                if (s[left] == oddChar)  ++prefOdd;
                if (s[left] == evenChar) ++prefEven;
            }

            int rightSt       = status(odd, even);
            int needLeftSt    = rightSt ^ 0b10;       // flip odd-parity bit only

            if (best[needLeftSt] != INT_MAX) {
                ans = max(ans, odd - even - best[needLeftSt]);
            }
        }
        return ans;
    }

public:
    int maxDifference(string s, int k) {
        int bestAns = INT_MIN;
        const vector<char> digs = {'0','1','2','3','4'};

        for (char odd : digs)
            for (char even : digs)
                if (odd != even) {
                    int cur = maxDiff(odd, even, s, k);
                    bestAns = max(bestAns, cur);
                }

        return bestAns == INT_MIN ? -1 : bestAns;
    }
};
