#include <iostream>
using namespace std;

const int maxi = 1000;
int adj[maxi][maxi];
bool visited[maxi];

void dfs(int V, int root) {
    visited[root] = true;
    cout << root << " ";
    for (int i = 0; i < V; ++i) {
        if (adj[root][i] == 1 && !visited[i]) {
            dfs(V, i);
        }
    }
}

int main() {
    int V, E;
    cin >> V;
    cin >> E;

    for (int i = 0; i < V; ++i) {
        for (int j = 0; j < V; ++j) {
            adj[i][j] = 0;
        }
    }

    for (int i = 0; i < E; ++i) {
        int node1, node2;
        cin >> node1 >> node2;
        adj[node1][node2] = 1;
        adj[node2][node1] = 1;
    }

    for (int i = 0; i < V; ++i) {
        visited[i] = false;
    }

    int root;
    cin >> root;

    dfs(V, root);
    cout << endl;

    return 0;
}
