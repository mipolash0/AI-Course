⏳ Iterative Deepening Search (IDS) in C++
📖 Overview
Iterative Deepening Search (IDS) combines the benefits of Depth-First Search's low memory usage with Breadth-First Search's completeness. IDS performs a series of Depth-Limited Searches (DLS) with increasing depth limits, starting from 0 and incrementing until the goal is found.

📌 Features
Interactive CLI: specify nodes, edges, graph type, start and goal

Repeatedly calls Depth-Limited Search with increasing depth limits

Guaranteed to find the shallowest goal node (optimal in terms of depth)

Low memory usage compared to BFS

Stops immediately when goal is found

🔧 How the Algorithm Works
Start with depth limit = 0.

Perform Depth-Limited Search (DLS) with current depth limit.

If goal found, stop and return.

Else increment depth limit and repeat.

Continue until goal is found or search exhausted.

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
Enter goal node: 5
🔽 Output
pgsql
Copy
Edit
IDS traversal starting from node 0:
Depth limit 0:
0
Depth limit 1:
0 1 2
Depth limit 2:
0 1 3 4 2
Depth limit 3:
0 1 3 5
Goal found at depth 3!
🚀 Applications
Domain	Use Case Example
AI Search	Optimal path search with limited memory
Robotics	Real-time pathfinding with depth cutoff
Puzzle Solving	Shallowest solution detection

⏱ Complexity
Metric	Complexity
Time	O(b^d) (repeated DFS)
Space	O(d) (recursion depth)

Time overhead due to repeated searches is generally acceptable due to exponential growth
