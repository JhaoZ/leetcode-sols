class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        std::unordered_set<int> visited;
        std::queue<int> q;
        q.push(0);
        visited.insert(0);
        while (!q.empty()) {
            auto current_room = q.front();
            q.pop();
            for (int key : rooms[current_room]) {
                if (visited.count(key)) {
                    continue;
                }
                visited.insert(key);
                q.push(key);
            }
        }

        return visited.size() == rooms.size();
    }
};