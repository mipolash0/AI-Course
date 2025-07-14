🔎 Depth-First Search (DFS) in C++
📖 Overview
Depth-First Search (DFS) is a fundamental graph traversal algorithm that explores as far as possible along each branch before backtracking. It is often used to explore connectivity, detect cycles, and perform topological sorting.

📌 Features
Interactive CLI: specify number of nodes, edges, and graph type (directed/undirected)

Supports recursive DFS traversal

Prints the order of node visits

Can be extended for cycle detection or path finding

Compact and easy to understand C++17 implementation

🔧 How the Algorithm Works
Start from a chosen start node.

Visit the node and mark it as visited.

Recursively visit all unvisited neighbors.

Backtrack when no unvisited neighbors remain.

Continue until all reachable nodes are visited.

🖥 Sample Input / Output
✅ Input
yaml
Copy
Edit
Enter number of nodes and edges: 6 7
Is the graph undirected? (1 for yes, 0 for no): 1
Enter edges:
0 1
0 2
1 3
1 4
2 4
3 5
4 5
Enter start node: 0
🔽 Output
csharp
Copy
Edit
DFS traversal starting from node 0:
0 1 3 5 4 2
🚀 Applications
Domain	Use Case Example
Graph theory	Connectivity, cycle detection
AI / Game Dev	Maze solving, puzzle exploration
Compilers	Topological sorting, syntax checking
Networking	Path exploration, network analysis

⏱ Complexity
Metric	Complexity
Time	O(V + E)
Space	O(V) (recursion + visited set)
