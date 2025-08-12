/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;
    
    Node() {
        val = false;
        isLeaf = false;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/

class Solution {
public:

    int isLeafNode(vector<vector<int>>& grid, std::pair<int, int>& start, std::pair<int, int>& end) {
        int curr = -1;
        for (int i = start.first; i < end.first; ++i) {
            for (int j = start.second; j < end.second; ++j) {
                if (curr == -1) {
                    curr = grid[i][j];
                    continue;
                }
                if (curr != grid[i][j]) {
                    return -1;
                }
            }
        }
        return curr;
    }

    Node* helper(vector<vector<int>>& grid, std::pair<int, int> start, std::pair<int, int> end, int n) {
        int val = isLeafNode(grid, start, end);
        if (val != -1) {
            Node* node = new Node(val, true);
            return node;
        }
        Node* node = new Node(val, false);
        node->topLeft = helper(grid, start, {end.first - (n/2), end.second - (n/2)}, n/2);
        node->topRight = helper(grid, {start.first, start.second + n / 2}, {end.first - (n/2), end.second}, n/2);
        node->bottomLeft = helper(grid, {start.first + n / 2, start.second}, {end.first, end.second - (n/2)}, n / 2);
        node->bottomRight = helper(grid, {start.first + n / 2, start.second + n / 2}, end, n / 2);
        return node;
    }

    Node* construct(vector<vector<int>>& grid) {
        int n = grid.size();
        return helper(grid, {0, 0}, {n, n}, n);
    }
};