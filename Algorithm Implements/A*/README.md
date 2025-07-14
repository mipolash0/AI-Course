
🌟 A* Search Algorithm – Full Explanation
🧠 Overview
A* (pronounced “A star”) is a widely used pathfinding and graph traversal algorithm. It is used to find the shortest path between two nodes in a graph. It combines the best features of Dijkstra's Algorithm and Greedy Best-First Search.

⚙️ How A* Works
The algorithm maintains a priority queue (often called the "open set") of nodes to be explored. Each node n in this queue is prioritized based on its evaluation function:

𝑓
(
𝑛
)
=
𝑔
(
𝑛
)
+
ℎ
(
𝑛
)
f(n)=g(n)+h(n)
Where:

g(n) = the exact cost to reach node n from the start node

h(n) = the heuristic estimated cost from node n to the goal

f(n) = estimated total cost of the cheapest solution through n

📦 Data Structures Used
Open Set: A priority queue (usually a min-heap) storing nodes to be explored, prioritized by f(n).

Closed Set: A set of nodes already explored.

Came From Map: A dictionary that helps in reconstructing the path once the goal is reached.

gScore Map: Maps nodes to their best-known cost from the start.

fScore Map: Maps nodes to their f(n) value.

🔁 Step-by-Step Algorithm
Initialize the open set with the start node.

Set g(start) = 0 and f(start) = h(start)

While the open set is not empty:

Remove the node current from the open set with the lowest f(n)

If current is the goal node:

Reconstruct the path using the "came from" map

Return the path

Move current to the closed set

For each neighbor n of current:

If n is in the closed set: continue

Calculate tentative gScore = g(current) + cost(current, n)

If this gScore is lower than any previously recorded g(n) for n:

Update cameFrom[n] = current

Update g(n) and f(n)

If n is not in the open set, add it

💡 Heuristic Function h(n)
The heuristic function estimates the cost from node n to the goal. It should be:

Admissible: Never overestimates the true cost.

Consistent (Monotonic): For all nodes n and their neighbors n', it holds:

ℎ
(
𝑛
)
≤
𝑐
𝑜
𝑠
𝑡
(
𝑛
,
𝑛
′
)
+
ℎ
(
𝑛
′
)
h(n)≤cost(n,n 
′
 )+h(n 
′
 )
Examples of heuristic functions:

Manhattan Distance (for grid maps)

Euclidean Distance

Chebyshev Distance

Domain-specific heuristics

🧮 Time and Space Complexity
Let:

b = branching factor (average number of children per node)

d = depth of the optimal solution

Then:

Time Complexity:

𝑂
(
𝑏
𝑑
)
O(b 
d
 )
In the worst case, A* explores every node.

Space Complexity:

𝑂
(
𝑏
𝑑
)
O(b 
d
 )
Because it stores all open and closed nodes.

🛠 Sample Input/Output for A* Search (Graph-based)
✅ Input:
yaml
Copy
Edit
Enter number of nodes: 4
Enter heuristic values for each node:
Node 1: 1 7
Node 2: 2 6
Node 3: 3 2
Node 4: 4 0
Enter number of edges: 4
Is the graph undirected? (1 for Yes, 0 for No): 1
Enter edges with cost (format: from to cost):
1 2 1
2 3 3
1 3 4
3 4 2
Enter start node: 1
Enter goal node: 4
(Note: The second value after each node number is its heuristic, e.g., node 1 has h=7, node 2 has h=6, etc.)

🕽 Output:
css
Copy
Edit
A* Path from 1 to 4: 1 2 3 4
📜 Explanation:
Step	Node	g(n)	h(n)	f(n) = g + h
Start	1	0	7	7
Move to 2	1+1 = 1	6	7	
Move to 3	1+3 = 4	2	6	
Move to 4	4+2 = 6	0	6	

Best total path: 1 → 2 → 3 → 4 with cost 6
