class Solution {
public:

    void dropdown(vector<vector<char>>& grid, int i, int j) {
        while (i + 1 < grid.size() && grid[i + 1][j] == '.') {
            grid[i][j] = '.';
            grid[i + 1][j] = '#';
            i++;
        }
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
                if (res[i][j] == '#') dropdown(res, i, j);
            }
        }

        return res;

    }
};