🔍 Best‑First Search (Greedy) in C++
📖 Overview
Greedy Best‑First Search (GBFS) is a graph search algorithm that expands the node closest to the goal, based only on the heuristic value h(n). It is similar in traversal style to A* and BFS, but prioritizes speed by ignoring actual path cost g(n), trading off optimality for efficiency.

📌 Key Features
✅ Interactive CLI: Specify number of nodes, edges, heuristic values, start and goal nodes.

✅ Uses min-heap (priority_queue with std::greater) to expand node with lowest h(n).

✅ Compatible with directed graphs (easily adaptable to undirected).

✅ Heuristic-driven traversal: visits promising nodes first.

✅ Prints each visited node and its heuristic value.

✅ Lightweight, portable C++17 implementation with STL only.

🔧 How the Algorithm Works
Initialize a priority queue with the start node.

While the queue is not empty:

Pop the node with the lowest heuristic value.

If this node is the goal, print success and terminate.

Otherwise, mark as visited and enqueue all unvisited neighbors with their heuristics.

If the queue becomes empty and the goal hasn't been found, the goal is unreachable.

🚫 Note: GBFS does not guarantee optimal paths, especially when heuristics are inaccurate.

🖥 Sample Input / Output
✅ Input:
less
Copy
Edit
Enter number of nodes and edges: 6 7
Enter heuristic values for each node:
Heuristic[0]: 10
Heuristic[1]: 8
Heuristic[2]: 5
Heuristic[3]: 7
Heuristic[4]: 3
Heuristic[5]: 0
Enter edges (u v):
0 1
0 2
1 3
1 4
2 4
4 5
3 5
Enter start and goal node: 0 5
🔽 Output:
pgsql
Copy
Edit
Visiting Node: 0 with Heuristic: 10
Visiting Node: 2 with Heuristic: 5
Visiting Node: 4 with Heuristic: 3
Visiting Node: 5 with Heuristic: 0
Goal Node 5 found!
🌐 Graph Overview
plaintext
Copy
Edit
     
    /    \
     
  /  \      \
    \
   \    /      \
     <------
Heuristic values in brackets h(n)

Path found: 0 → 2 → 4 → 5

🚀 Applications
Field	Use Case Example
🚗 Route Planning	GPS: find a quick path even if not optimal
🕹 Game AI	NPC pathfinding with limited CPU budget
🌐 Web Crawling	Heuristic-guided site exploration
🤖 Robotics	Quick motion planning in dynamic environments
🧠 AI Search Problems	Fast approximations for complex combinatorial spaces

⏱ Time & Space Complexity
Metric	Complexity
Time	O(E · log V) – due to priority queue ops
Space	O(V) – for visited nodes and queue

⚠️ Heuristic quality greatly influences performance.
