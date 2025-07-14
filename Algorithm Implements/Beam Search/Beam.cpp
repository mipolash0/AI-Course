
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
    int n, e, start, goal, beam_width;
    cin >> n >> e;

    vector<int> heuristic(n);
    vector<vector<int>> graph(n);

    for (int i = 0; i < n; ++i) cin >> heuristic[i];
    for (int i = 0; i < e; ++i) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
    }

    cin >> start >> goal >> beam_width;

    queue<int> q;
    q.push(start);

    while (!q.empty()) {
        vector<int> next_level;
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            if (node == goal) {
                cout << "Goal: " << node;
                return 0;
            }
            for (int v : graph[node]) next_level.push_back(v);
        }
        sort(next_level.begin(), next_level.end(), [&](int a, int b) { return heuristic[a] < heuristic[b]; });
        for (int i = 0; i < min(beam_width, (int)next_level.size()); ++i) q.push(next_level[i]);
    }

    cout << "Goal not found.";
    return 0;
}
