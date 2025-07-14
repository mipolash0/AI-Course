❌⭕ Tic-Tac-Toe with Smart AI (Minimax) — Play & Challenge Your Brain!
Welcome to this classic Tic-Tac-Toe game with a twist: the computer opponent uses the Minimax algorithm with alpha-beta pruning to make smart moves! Whether you’re a beginner or just want a fun challenge, this game has you covered.

🎯 Game Highlights
Interactive GUI: Built with Tkinter for a simple and clean interface.

Player vs Computer: You play as X, AI plays as O.

Intelligent AI: Uses Minimax algorithm to plan ahead and block or win.

Alpha-Beta Pruning: Speeds up AI decisions without compromising strategy.

Draw & Win Detection: Automatically detects wins, losses, and draws.

Responsive Design: Buttons disable after moves to prevent errors.

🚀 How to Play
Run the game:

bash
Copy
Edit
python tic_tac_toe.py
Click on any empty square to place your X.

The computer will automatically respond with its move O.

Try to beat the AI or settle for a draw!

🧠 Behind the Scenes
The board is a 3x3 grid controlled by buttons.

Each move updates the board state.

The Minimax algorithm evaluates all possible future moves up to a limited depth (2 moves ahead) for the AI.

The AI chooses moves to maximize its chance of winning or drawing.

Alpha-beta pruning optimizes the Minimax to skip unnecessary branches, making AI moves faster.

⚙️ Customization
Change depth in minimax() for harder or easier AI.

Adjust board size or win length (currently 3x3, 3 in a row to win).

Enhance UI with colors or animations.
