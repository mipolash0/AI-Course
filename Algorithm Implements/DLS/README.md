⏳ Depth-Limited Search (DLS) in C++
📖 Overview
Depth-Limited Search (DLS) is a variation of Depth-First Search (DFS) that limits the depth of the search to a specified limit L. It explores nodes only up to depth L, preventing infinite descent in infinite or very deep graphs. DLS is useful in iterative deepening and when the search space is large or infinite.

📌 Features
Interactive CLI: define nodes, edges, graph type (directed/undirected), start node, and depth limit

Recursive DFS variant with depth cutoff

Prints visited nodes within the depth limit

Stops exploring deeper nodes beyond limit

🔧 How the Algorithm Works
Start DFS from the start node with initial depth = 0.

Visit the node and mark it.

If current depth == limit, backtrack (stop exploring deeper).

Otherwise, recursively explore all unvisited neighbors with depth + 1.

Continue until all reachable nodes within depth limit are visited.

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
Enter depth limit: 2
🔽 Output
css
Copy
Edit
DLS traversal from node 0 up to depth 2:
0 1 3 4 2
🚀 Applications
Domain	Use Case Example
Search Algorithms	Iterative deepening search (IDS) base
AI / Game Search	Cutoff infinite search spaces
Robotics	Limit search depth to control cost

⏱ Complexity
Metric	Complexity
Time	O(b^L), where b=branching factor, L=depth limit
Space	O(L) due to recursion stack
