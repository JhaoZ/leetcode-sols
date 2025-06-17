class Solution {
public:

    void dropdown(vector<vector<char>>& grid, int i, int j) {
        
    }

    vector<vector<char>> rotateTheBox(vector<vector<char>>& boxGrid) {
        vector<vector<char>> res(boxGrid[0].size(), vector<char>(boxGrid.size(), '.'));

        for (int i = 0; i < boxGrid.size(); ++i) {
            for (int j = 0; j < boxGrid[i].size(); ++j) {
                res[j][i] = boxGrid[boxGrid.size() - i - 1][j];
            }
        }

        for (int i = res.size() - 1; i >= 0; --i) {
            for (int j = 0; j < res[i].size(); ++j) {
                if (res[i][j] == '#') {
                    int ii = i;
                    int jj = j;
                    while (ii + 1 < res.size() && res[ii + 1][j] == '.') {
                        res[ii][jj] = '.';
                        res[ii + 1][jj] = '#';
                        ii++;
                    }
                }
            }
        }

        return res;

    }
};