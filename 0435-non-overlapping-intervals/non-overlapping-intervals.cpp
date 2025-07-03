class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const vector<int>& l, const vector<int>& r) {
            return l[0] == r[0] ? l[1] < r[1] : l[0] < r[0];
        });

        int ans = 0;
        stack<vector<int>> s;
        for (int i = 0; i < intervals.size(); ++i) {
            if (s.empty()) {
                s.push(intervals[i]);
            } else {
                auto last = s.top();
                if (intervals[i][0] < last[1]) {
                    if (intervals[i][1] < last[1]) {
                        s.pop();
                        s.push(intervals[i]);
                    }
                } else {
                    s.push(intervals[i]);
                }
            }
        }
        return intervals.size() - s.size();

    }
};