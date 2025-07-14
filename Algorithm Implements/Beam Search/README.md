🔦 Beam Search Algorithm in C++
📖 Overview
Beam Search is a heuristic-based, memory-bounded search algorithm that explores graphs level by level, similar to Breadth-First Search (BFS). However, instead of exploring all nodes at each level, it restricts itself to only the most promising w nodes, where w is the beam width.

This balances the breadth of search with computational efficiency, allowing it to scale to large graphs while maintaining a bias toward promising paths.

📌 Features
✅ Interactive CLI: Input nodes, edges, heuristics, beam width

✅ Heuristic-guided pruning at every level

✅ Supports directed graphs of arbitrary size

✅ Reports success or failure based on goal reachability

✅ Clear traversal output and pruning behavior

✅ Header-only C++17 compatible for easy embedding

🔧 How the Algorithm Works
Initialize the queue Q with the start node

While Q is not empty:

Expand all nodes in Q to get the next_level frontier

Sort next_level by heuristic value h(n) (ascending)

Trim next_level to beam width w

If goal is among nodes, ✅ success

Replace Q with trimmed next_level

If the queue empties and goal not found, ❌ failure

🖥 Sample Input / Output
✅ Input:
mathematica
Copy
Edit
Enter number of nodes and edges: 7 8
Enter heuristic values:
10 8 5 7 3 2 0
Enter edges (u v):
0 1
0 2
1 3
1 4
2 4
2 5
4 6
5 6
Enter start, goal, and beam width: 0 6 2
🔽 Output:
vbnet
Copy
Edit
Exploring: 0
Next level: 1 (h=8), 2 (h=5)
Exploring: 2
Next level: 4 (h=3), 5 (h=2)
Exploring: 5
Next level: 6 (h=0)
Goal found at node 6
🌍 Visual Representation of the Graph
vbnet
Copy
Edit
Nodes (with h(n)):
0(10), 1(8), 2(5), 3(7), 4(3), 5(2), 6(0)

Edges:
0 → 1, 2
1 → 3, 4
2 → 4, 5
4 → 6
5 → 6
Path Taken: 0 → 2 → 5 → 6

🚀 Applications of Beam Search
Domain	Use Case Example
🔤 NLP	Machine translation, sentence decoding (e.g., Transformers)
🗣 Speech Recognition	Word/phoneme sequence prediction
🎮 Game AI	Lookahead with limited width (chess-like games)
🤖 Robotics	Resource-constrained pathfinding
📦 Optimization Problems	Heuristic pruning in NP-hard problems (e.g., TSP, scheduling)

⏱ Complexity Analysis
Metric	Complexity
Time	O(w · d · b) — beam width × depth × branch factor
Space	O(w · d) — memory proportional to beam × depth

⚠️ Beam Search trades optimality for efficiency

Small width: fast but may miss best path

Large width: more accurate, closer to BFS cost

📄 Code Structure Overview
cpp
Copy
Edit
main()               → Reads input and initiates beam search
beam_search()        → Core algorithm with frontier trimming
heuristic[]          → h(n) for each node
adjacency list       → graph[u] holds all outgoing edges from u
✅ Dependencies
Standard C++17

Headers used: iostream, vector, queue, algorithm

🧪 Compile & Run
🛠 Compile:
bash
Copy
Edit
g++ beam_search.cpp -o beam_search
▶️ Run:
bash
Copy
Edit
./beam_search
