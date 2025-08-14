class Leaderboard {
public:

    std::unordered_map<int, int> board;
    std::multiset<int, std::greater<int>> data;
    Leaderboard() {}
    
    void addScore(int playerId, int score) {
        int oldscore = -1;
        if (board.count(playerId)) {
            oldscore = board[playerId];
            board[playerId] += score;
        } else {
            board[playerId] = score;
        }
        if (oldscore != -1) {
            data.erase(data.find(oldscore));
        }
        data.insert(board[playerId]);
    }
    
    int top(int K) {
        int sum = 0;
        auto it = data.begin();
        for (int i = 0; i < K; i++) {
            sum += *it;
            it++;
        }
        return sum;
    }
    
    void reset(int playerId) {
        data.erase(data.find(board[playerId]));
        board.erase(playerId);
    }
};

/**
 * Your Leaderboard object will be instantiated and called as such:
 * Leaderboard* obj = new Leaderboard();
 * obj->addScore(playerId,score);
 * int param_2 = obj->top(K);
 * obj->reset(playerId);
 */