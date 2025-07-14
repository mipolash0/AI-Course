🔍 Breadth‑First Search (BFS) in C++
📖 Overview
Breadth‑First Search (BFS) is a classic algorithm used to explore graphs level by level, ideal for finding the shortest path in unweighted graphs. It uses a queue and tracks visited nodes to avoid cycles or repeated visits.

📌 Features
✅ Interactive CLI: define number of nodes and edges

✅ Option to choose directed or undirected graph

✅ Accepts custom edge input

✅ Displays full shortest path from start to goal node

✅ Uses queue of paths for automatic path reconstruction

✅ Includes graph printing for debugging or visualization

🔧 How the Algorithm Works
Start by pushing a path [start] into a queue

While queue is not empty:

Pop the front path

Get the last node in the path

If it's the goal, return the path

For each unvisited neighbor of the last node:

Copy the path and add the neighbor

Push the new path into the queue

If goal is not reachable, return no path

🖥 Sample Input / Output
✅ Input:
yaml
Copy
Edit
Enter number of nodes: 6
Enter number of edges: 7
Is the graph undirected? (1 for Yes, 0 for No): 1
Enter edges (format: from to):
0 1
0 2
1 3
1 4
2 4
3 5
4 5
Enter start node: 0
Enter goal node: 5
🔽 Output:
yaml
Copy
Edit
Graph structure:
0: 1 2 
1: 0 3 4 
2: 0 4 
3: 1 5 
4: 1 2 5 
5: 3 4 

BFS Path from 0 to 5: 0 1 3 5
🚀 Applications of BFS
Domain	Use Case
Shortest Path	Fastest path in unweighted graphs
Network Analysis	Check if a graph is connected
AI & Robotics	Planning/exploration of unweighted spaces
Social Networks	Degrees of connection between users
Web Crawlers	Level-order exploration of linked pages

⏱ Complexity Analysis
Metric	Complexity
Time	O(V + E)
Space	O(V)

📄 Code Structure
cpp
Copy
Edit
int main()
→ Handles input and calls bfs()

void bfs()
→ BFS logic using queue of paths, prints full path

void printGraph()
→ Prints adjacency list
✅ Dependencies
C++17 Standard

Headers: iostream, vector, queue, unordered_map, unordered_set

🧪 Compile & Run
🛠️ Compile:
bash
Copy
Edit
g++ bfs.cpp -o bfs
▶️ Run:
bash
Copy
Edit
./bfs
