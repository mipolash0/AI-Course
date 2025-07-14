#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int minimax(int depth, int index, bool is_max, const vector<int>& scores, int h) {
    return (depth == h) ? scores[index] : is_max
        ? max(minimax(depth+1, index*2, false, scores, h),
              minimax(depth+1, index*2+1, false, scores, h))
        : min(minimax(depth+1, index*2, true, scores, h),
              minimax(depth+1, index*2+1, true, scores, h));
}

int main() {
    int h;
    cin >> h;
    int leaf_nodes = 1 << h;
    vector<int> scores(leaf_nodes);
    for (int& score : scores) cin >> score;
    cout << minimax(0, 0, true, scores, h);
    return 0;
}
