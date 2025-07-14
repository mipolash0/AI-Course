♟️ Chess: Player vs Computer (Minimax AI) in Python with Pygame
Welcome to a classic game of Chess powered by AI! This project brings you a fully playable chess game where you face off against a computer opponent using the Minimax algorithm with alpha-beta pruning — a fundamental AI technique for game decision making.

🎮 Features
Intuitive GUI: Beautiful chessboard rendered using Pygame, complete with piece symbols and move highlights.

Player vs Computer: You play as White; the computer controls Black.

Minimax AI: The computer plans ahead by simulating possible moves to make intelligent decisions.

Alpha-Beta Pruning: Optimizes AI move calculation for better performance.

Pawn Promotion: Automatic handling of pawn promotion to Queen, Rook, Bishop, or Knight.

Game End Detection: Detects checkmate, stalemate, draws (including 75-move rule and repetition).

Move Hints & Highlights: Visual feedback for selected piece and legal moves.

⚙️ How It Works
Pygame Board Rendering:
The board is drawn with alternating colors, chess pieces as Unicode symbols, and selected squares & legal moves highlighted.

Player Interaction:
You select a piece with a click, legal moves are shown, and clicking a valid destination makes your move.

AI Opponent:
The AI uses a Minimax search with depth 1 (looking one move ahead) and alpha-beta pruning to choose the best move. You can easily adjust difficulty by changing the depth.

Game Logic:
Using the python-chess library to manage board state, legal moves, check/checkmate detection, and special rules.

Game Over:
When the game ends, the result is displayed on screen for 4 seconds before closing.

🕹️ How to Play
Run the game using:

bash
Copy
Edit
python chess_minimax.py
Click on a white piece to select it.

Legal moves will be highlighted with green dots.

Click on a highlighted square to move.

Play until checkmate or draw.

The AI will respond automatically.

🔧 Requirements
Python 3.x

pygame library

python-chess library

Install dependencies via pip:

bash
Copy
Edit
pip install pygame python-chess
🎯 Customize & Improve
Increase AI strength by raising minimax depth in the code.

Add move timers or difficulty settings.

Implement advanced heuristics for smarter AI.

Improve UI/UX with animations or sound effects.
