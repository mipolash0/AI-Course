🔄 AO* (Hill-Climbing-Style) Search in C++
📖 Overview
The AO* (And-Or) search algorithm—when implemented in a simplified Greedy Hill-Climbing style—is a heuristic-based search technique used to traverse directed graphs. It continuously selects the neighbor with the lowest heuristic value and moves forward only if there's a better choice, effectively climbing "downhill" in heuristic space.

This variant does not backtrack, meaning it may stop at a local optimum, making it faster but not always globally optimal.

📌 Key Features
✅ Interactive CLI: Input nodes, heuristic values, and edges

✅ Accepts custom directed graphs

✅ Traverses using greedy descent on heuristic values

✅ Prints full traversal path

✅ Identifies and displays local minimum (peak)

✅ Minimal dependencies; C++17 compliant, no external libraries

✅ Fast and compact code, ideal for AI demonstrations

🔧 How the Algorithm Works
This implementation follows a Greedy Hill-Climbing approach:

Start at the initial node (current)

Check all neighbors of current

Among all neighbors, pick the one with the smallest heuristic value that is strictly less than the current

Move to that neighbor

Repeat steps 2–4 until no neighbor has a better (lower) heuristic

Terminate at the local minimum (a peak in heuristic descent)

Unlike complete search algorithms (like A*, DFS, or BFS), this version of AO* is greedy and does not explore multiple paths or maintain memory of explored nodes.

🧠 AO* and Hill Climbing
AO* search typically supports AND/OR trees and backtracking

This simplified version represents the hill-climbing component of AO*

This version demonstrates local search and greedy decision-making

🖥 Sample Input / Output
✅ Input:
mathematica
Copy
Edit
Enter number of nodes: 5
Enter heuristic values:
7 6 3 1 0
Enter number of edges: 6
Enter edges (u v):
0 1
0 2
1 3
2 3
3 4
1 4
Enter start node: 0
🔽 Output:
sql
Copy
Edit
Current: 0 with h=7
Current: 2 with h=3
Current: 3 with h=1
Current: 4 with h=0
Reached peak at node: 4
🌍 Graph Visualization
plaintext
Copy
Edit
       (0)[7]
      /     \
  (1)[6]   (2)[3]
   |   \     |
  (3)[1]    /
     |
   (4)[0]
Heuristic values shown in brackets [h(n)]

Traversal: 0 → 2 → 3 → 4

🚀 Real-World Applications
Field	Use Case
🤖 AI Planning	Task planning with heuristic goals
🛰️ Robotics	Local navigation, obstacle avoidance
📦 Operations R&D	Route optimization, scheduling with greedy strategies
🧠 Machine Learning	Hyperparameter tuning with local optimization
🎮 Game AI	Simple decision trees with no backtracking

⏱ Complexity Analysis
Metric	Complexity
Time	O(V + E) — all nodes & edges visited once
Space	O(V) — for heuristic and graph storage

⚠️ Limitation: May converge to local minima if no better neighbor is available (no backtracking or randomness)

📄 Code Structure
cpp
Copy
Edit
int main()
→ Collects user input and initiates hill-climbing search

vector<int> heuristic
→ Stores h(n) heuristic value for each node

vector<vector<int>> graph
→ Adjacency list to represent the directed graph

Greedy loop
→ Iteratively moves to best neighbor until stuck
✅ Dependencies
C++17 standard

Uses: iostream, vector, limits

🧪 Try It Yourself
🛠 Compile:
bash
Copy
Edit
g++ ao_star.cpp -o ao_star
▶️ Run:
bash
Copy
Edit
./ao_star
Provide node/edge data when prompted to observe greedy heuristic descent.
