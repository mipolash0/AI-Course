
import pygame
import sys
import time
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
GRID_SIZE = 5
CELL_SIZE = WIDTH // GRID_SIZE
TIMER_DURATION = 15

# Emojis
PLAYER1 = "🧍"
LIZARD = "🦎"
EMPTY = "⬜"

# Colors
BACKGROUND_COLOR = (173, 216, 230)  # Light blue
FONT_COLOR = (0, 100, 0)            # Dark green

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch Sanda - Emoji Grid (1 Player)")
font = pygame.font.SysFont("Segoe UI Emoji", CELL_SIZE - 10)
timer_font = pygame.font.SysFont("Arial", 24)

class Game:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.player1_pos = [0, 0]
        self.lizard_pos = [GRID_SIZE - 1, GRID_SIZE - 1]
        self.start_time = time.time()
        self.game_over = False
        self.winner = None
        self.turn = "player1"

    def draw_grid(self):
        screen.fill(BACKGROUND_COLOR)

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                symbol = EMPTY
                if [row, col] == self.player1_pos:
                    symbol = PLAYER1
                elif [row, col] == self.lizard_pos:
                    symbol = LIZARD

                text = font.render(symbol, True, FONT_COLOR)
                rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2,
                                             row * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text, rect)

        elapsed = int(time.time() - self.start_time)
        remaining = max(0, TIMER_DURATION - elapsed)
        timer_text = timer_font.render(f"Time left: {remaining}s", True, FONT_COLOR)
        screen.blit(timer_text, (10, HEIGHT - 30))

        if self.game_over:
            msg = f"{self.winner} caught the 🦎!" if self.winner else "The 🦎 escaped!"
            result = timer_font.render(msg, True, FONT_COLOR)
            screen.blit(result, (WIDTH // 2 - 120, HEIGHT // 2 - 20))
            restart = timer_font.render("Press R to restart", True, FONT_COLOR)
            screen.blit(restart, (WIDTH // 2 - 100, HEIGHT // 2 + 20))

    def move_player(self, direction):
        if self.game_over:
            return

        y, x = self.player1_pos
        if direction == "UP" and y > 0:
            y -= 1
        elif direction == "DOWN" and y < GRID_SIZE - 1:
            y += 1
        elif direction == "LEFT" and x > 0:
            x -= 1
        elif direction == "RIGHT" and x < GRID_SIZE - 1:
            x += 1

        self.player1_pos = [y, x]
        self.turn = "ai"
        self.check_end_conditions()

    def move_ai(self):
        if self.turn != "ai" or self.game_over:
            return

        best_move = self.lizard_pos[:]
        max_dist = self.distance(self.lizard_pos, self.player1_pos)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dy, dx in directions:
            ny = self.lizard_pos[0] + dy
            nx = self.lizard_pos[1] + dx
            if 0 <= ny < GRID_SIZE and 0 <= nx < GRID_SIZE:
                new_pos = [ny, nx]
                dist = self.distance(new_pos, self.player1_pos)
                if dist > max_dist:
                    best_move = new_pos
                    max_dist = dist

        self.lizard_pos = best_move
        self.turn = "player1"
        self.check_end_conditions()

    def distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def check_end_conditions(self):
        if self.player1_pos == self.lizard_pos:
            self.game_over = True
            self.winner = "Player"
        elif time.time() - self.start_time > TIMER_DURATION:
            self.game_over = True
            self.winner = None

def main():
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game.game_over:
                    game.reset_game()
                if not game.game_over and game.turn == "player1":
                    if event.key == pygame.K_UP:
                        game.move_player("UP")
                    elif event.key == pygame.K_DOWN:
                        game.move_player("DOWN")
                    elif event.key == pygame.K_LEFT:
                        game.move_player("LEFT")
                    elif event.key == pygame.K_RIGHT:
                        game.move_player("RIGHT")

        if game.turn == "ai" and not game.game_over:
            game.move_ai()

        game.draw_grid()
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
