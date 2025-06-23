class Solution {
public:

    bool func(int n, int k) {
        if (n == 1) {
            return false;
        }

        if (k % 2 == 1) {
            return func(n - 1, (k + 1) / 2);
        } else {
            return !func(n - 1, (k + 1) / 2);
        }
    }

    int kthGrammar(int n, int k) {
        return func(n, k) ? 1 : 0;
    }
};