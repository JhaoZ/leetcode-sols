class Solution {
public:
    int minMaxDifference(int num) {

        int max_num = num;
        int min_num = num;
        vector<string> ref;
        while (num > 0) {
            ref.push_back(to_string(num % 10));
            num /= 10;
        }

        auto eval = [](const vector<string>& t) {
            int n = 0;
            for (int i = 0; i < t.size(); ++i) n += stoi(t[i]) * pow(10, i);
            return n;
        };

        for (int i = 0; i < 10; ++i) {
            for (int j = 0; j < 10; ++j) {
                vector<string> t(ref);
                for (int ii = 0; ii < t.size(); ++ii) {
                    if (stoi(t[ii]) == i) {
                        t[ii] = to_string(j);
                    }
                }
                auto e = eval(t);
                max_num = max(max_num, e);
                min_num = min(min_num, e);

            }
        }
        cout << max_num << endl;
        cout << min_num << endl;
        return max_num - min_num;
        
    }
};