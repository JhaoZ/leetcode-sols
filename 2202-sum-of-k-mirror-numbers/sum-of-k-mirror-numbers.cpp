class Solution {

using ll = long long;

public:

    bool isPal(int k, ll num) {
        vector<ll> temp;
        while (num > 0) {
            temp.push_back(num % k);
            num /= k;
        } 
        vector<ll> other(temp);
        reverse(other.begin(), other.end());
        for (size_t i = 0; i < other.size(); ++i) {
            if (other[i] != temp[i]) return false;
        }
        return true;
    }
 
    ll kMirror(int k, int n) {
        ll ans = 0;
        int counted = 0;
        int left = 1;
        int right = 1;
        while (counted < n) {
            right = left * 10;
            // try 2 * d - 1 digits

            for (int j = 0; j <= 1; ++j) {
                for (int i = left; i <= right; ++i) {
                    ll curr = j == 0 ? i / 10 : i;
                    ll temp = i;
                    
                    while (temp) {
                        curr = curr * 10 + (temp % 10);
                        temp /= 10;
                    }

                    if (isPal(k, curr)) {
                        ans += curr;
                        counted++;
                    }

                    if (counted >= n) {
                        break;
                    }
                }
            }
            left = right;

        }
        return ans;
    }
};