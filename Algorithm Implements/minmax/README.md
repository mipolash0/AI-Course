♟️ Minimax Algorithm in C++
📖 Overview
Minimax is a decision rule used for minimizing the possible loss for a worst-case scenario. It is widely used in two-player, zero-sum games (e.g., Tic-Tac-Toe, Chess) where players alternate turns — one tries to maximize the score (Maximizer), the other tries to minimize it (Minimizer).

📌 Features
Simple recursive implementation

Evaluates game states to choose optimal moves

Alternates between maximizing and minimizing players

Works for games with clear win/loss/draw outcomes

🔧 How the Algorithm Works
At each node:

If leaf node (end of game), return heuristic score

If Maximizer’s turn: choose the move with the maximum value

If Minimizer’s turn: choose the move with the minimum value

Propagate values up the tree to choose the best move

🖥 Sample Input / Output
For a simple fixed game tree:

yaml
Copy
Edit
Max chooses best outcome: 3
📄 Code Structure
minimax() – Recursive function returning best score for current player

main() – Demonstrates minimax on a sample game tree

✅ Dependencies
Standard C++17: iostream, vector, algorithm
