♟️ Minimax with Alpha–Beta Pruning in C++
🧠 What is Alpha–Beta Pruning?
Alpha–Beta Pruning is an optimization of the Minimax algorithm used in two-player, perfect-information games such as Chess, Checkers, and Tic-Tac-Toe. It reduces the number of nodes evaluated in the game tree, enabling faster and more efficient decision-making.

📌 Features
✅ Interactive CLI—enter tree height and leaf node scores

✅ Complete binary tree automatically constructed

✅ Maximizer and Minimizer turns alternate properly

✅ Efficient pruning using α (alpha) and β (beta) bounds

✅ Console output shows optimal value and pruning action

🔧 How the Algorithm Works
🧠 Minimax Recap
The Minimax algorithm explores all game outcomes, assuming both players play optimally. The Maximizer tries to get the highest possible score, while the Minimizer tries to minimize it.

🚀 Alpha–Beta Optimization
Alpha (α): Best (maximum) value that the Maximizer can guarantee so far

Beta (β): Best (minimum) value that the Minimizer can guarantee so far

Pruning Logic
At Max nodes:

nginx
Copy
Edit
alpha = max(alpha, best_value);
if alpha >= beta: prune (no need to explore further)
At Min nodes:

matlab
Copy
Edit
beta = min(beta, best_value);
if beta <= alpha: prune
This ensures unnecessary branches are skipped, improving efficiency without affecting the result.

🖥 Sample Input / Output
✅ Input:
yaml
Copy
Edit
Enter height of the game tree: 3
Enter 8 leaf node values:
3 17 2 12 15 25 2 5
🔽 Output:
csharp
Copy
Edit
Optimal value with alpha-beta pruning: 12
🧠 Example Tree (Height 3)
markdown
Copy
Edit
                     MAX
                    /   \
                 MIN     MIN
               /   \     /   \
             MAX   MAX  MAX  MAX
            / \   / \   / \   / \
           3  17  2 12 15 25  2  5
🚀 Applications
Domain	Use Case
🎮 Game AI	Chess (Stockfish), Checkers, Tic-Tac-Toe, Connect-Four
🤖 Robotics	Adversarial planning, competitive simulations
🔐 Security	Attack/Defense planning in intrusion detection systems
💼 Economics	Competitive bidding or adversarial market strategies
🧪 Research/R&D	Optimizing decision trees in adversarial environments

⏱ Complexity Analysis
Metric	Complexity
Time (No Pruning)	O(b^d)
Time (Best Case)	O(b^(d/2)) with perfect pruning
Space	O(b·d) (recursion stack + evaluation)
