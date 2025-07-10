class Solution {
public:
    int maxFreeTime(int eventTime, vector<int>& startTime, vector<int>& endTime) {
        std::multiset<int> spaces;

        struct cand {
            int start_space{0};
            int end_space{0};
            int block{0};
        };

        std::vector<cand> cands;
        int prev_space = -1;
        int blocked = 0;
        int prev = 0;
        for (int i = 0; i < startTime.size(); ++i) {
            int curr_start = startTime[i];
            int curr_end = endTime[i];
            spaces.insert(curr_start - prev);
            if (prev_space != -1) {
                cands.push_back({prev_space, curr_start - prev, endTime[i - 1] - startTime[i - 1]});
            }
            blocked = endTime[i ] - startTime[i];
            prev_space = curr_start - prev;
            prev = curr_end;
        }
        spaces.insert(eventTime - prev);
        cands.push_back({prev_space, eventTime - prev, blocked});

        int ans = 0;
        for (const auto& cand : cands) {
            auto [start, end, block] = cand;
            auto it = spaces.find(start);
            spaces.erase(it);
            it = spaces.find(end);
            spaces.erase(it);

            it = spaces.lower_bound(block); // can we fit block into another place?
            if (it != spaces.end()) {
                // yes we can
                ans = max(ans, start + end + block);
            }
            ans = max(ans, start + end);
            
            spaces.insert(start);
            spaces.insert(end);
        }
        return ans;


    }
};