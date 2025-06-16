class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {

        if (target == source) {
            return 0;
        }

        unordered_map<int, vector<int>> graph;
        unordered_map<int, unordered_set<int>> children;
        

        for (int i = 0; i < routes.size(); ++i) {
            unordered_set<int> curr;

            for (int j = 0; j < routes[i].size(); ++j) {
                curr.insert(routes[i][j]);
            }

            children[i] = curr;

            for (int j = 0; j < routes.size(); ++j) {
                if (i != j) {
                    for (const auto& n : routes[j]) {
                        if (children[i].count(n)) {
                            graph[i].push_back(j);
                            break;
                        }
                    }
                }
            }
        }

        queue<pair<int, int>> q;
        unordered_set<int> visited;
        for (int i = 0; i < routes.size(); ++i) {
            if (children[i].count(source)) {
                q.push({i, 1});
                visited.insert(i);
            }
        } 

        while (!q.empty()) {
            auto [bus, dist] = q.front();
            q.pop();

            if (children[bus].count(target)) {
                return dist;
            }

            for (const auto& n : graph[bus]) {
                if (visited.count(n)) {
                    continue;
                }
                visited.insert(n);
                q.push({n, dist + 1});
            }
            

        }

        return -1;
        

        

        
    }
};