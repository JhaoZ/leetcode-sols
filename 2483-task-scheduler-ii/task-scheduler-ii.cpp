class Solution {
public:
    long long taskSchedulerII(vector<int>& tasks, int space) {
        unordered_map<long long, long long> times;
        long long day = 0;
        int task_idx = 0;
        while (task_idx < tasks.size()) {
            int t = tasks[task_idx];
            if (times.count(t) && (day - times[t] <= space)) {
               day = times[t] + space + 1;
               times[t] = day;
               task_idx++;
            } else {
                day++;
                times[t] = day;
                task_idx++;
            }
        }
        return day;


    }
};