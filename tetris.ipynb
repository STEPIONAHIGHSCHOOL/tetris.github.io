import pygame
import random

# Window and block settings
Screen_Width = 300
Screen_Height = 600
Block_size = 30
Board_width = Screen_Width // Block_size
Board_Height = Screen_Height // Block_size
FPS = 20  # game frames per second

# Tetromino shapes and colors
SHAPES = [
    [[1,1,1,1]],          # I
    [[1,1],[1,1]],        # O
    [[1,1,0],[0,1,1]],    # S
    [[0,1,1],[1,1,0]],    # Z
    [[1,1,1],[0,1,0]],    # T
    [[1,1,1],[1,0,0]],    # L
    [[1,1,1],[0,0,1]]     # J
]
COLORS = [
    (0,255,255),  # Cyan
    (255,255,0),  # Yellow
    (0,255,0),    # Green
    (255,0,0),    # Red
    (255,0,255),  # Magenta
    (255,165,0),  # Orange
    (0,0,255)     # Blue
]

class GameTetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Screen_Width, Screen_Height))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.board = [[0]*Board_width for _ in range(Board_Height)]
        self.gameover = False

        self.tetromino = self.new_tetromino()
        self.next_tetromino = self.new_tetromino()
        self.x, self.y = Board_width // 2, 0

        self.fall_time = 0
        self.level = 1
        self.score = 0
        self.lines_cleared = 0

    def new_tetromino(self):
        shape = random.choice(SHAPES)
        color = COLORS[SHAPES.index(shape)]
        return {'shape': shape, 'color': color}

    def valid_position(self, dx=0, dy=0, shape=None):
        if shape is None:
            shape = self.tetromino['shape']
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.x + x + dx
                    new_y = self.y + y + dy
                    if new_x < 0 or new_x >= Board_width or new_y >= Board_Height:
                        return False
                    if new_y >= 0 and self.board[new_y][new_x]:
                        return False
        return True

    def merge_tetromino(self):
        shape = self.tetromino['shape']
        color = self.tetromino['color']
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell and self.y + y >= 0:
                    self.board[self.y + y][self.x + x] = COLORS.index(color) + 1

    def clear_lines(self):
        new_board = []
        lines_cleared = 0
        for row in self.board:
            if all(row):
                lines_cleared += 1
            else:
                new_board.append(row)
        for _ in range(lines_cleared):
            new_board.insert(0, [0]*Board_width)
        self.board = new_board

        self.lines_cleared += lines_cleared
        self.score += lines_cleared * 100

        if self.lines_cleared // 10 >= self.level:
            self.level += 1

    def rotate_tetromino(self):
        shape = self.tetromino['shape']
        rotated = [list(row) for row in zip(*shape[::-1])]
        if self.valid_position(shape=rotated):
            self.tetromino['shape'] = rotated

    def move(self, dx, dy):
        if self.valid_position(dx, dy):
            self.x += dx
            self.y += dy
        elif dy:  # hit bottom
            self.merge_tetromino()
            self.clear_lines()
            self.tetromino = self.next_tetromino
            self.next_tetromino = self.new_tetromino()
            self.x, self.y = Board_width // 2, 0
            if not self.valid_position():
                self.gameover = True

    def draw_board(self):
        self.screen.fill((0,0,0))
        # Draw locked blocks
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    color = COLORS[cell-1]
                    pygame.draw.rect(self.screen, color, (x*Block_size, y*Block_size, Block_size, Block_size))
        # Draw current tetromino
        shape = self.tetromino['shape']
        color = self.tetromino['color']
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    px = (self.x + x) * Block_size
                    py = (self.y + y) * Block_size
                    pygame.draw.rect(self.screen, color, (px, py, Block_size, Block_size))
        self.draw_grid()
        self.draw_text(f"Score: {self.score}", 18, (255,255,255), 10, 10)
        self.draw_text(f"Level: {self.level}", 18, (255,255,255), 10, 40)
        pygame.display.flip()

    def draw_grid(self):
        for x in range(Board_width):
            pygame.draw.line(self.screen,(50,50,50),(x*Block_size,0),(x*Block_size,Screen_Height))
        for y in range(Board_Height):
            pygame.draw.line(self.screen,(50,50,50),(0,y*Block_size),(Screen_Width,y*Block_size))

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.SysFont("comicsansms", size)
        label = font.render(text, True, color)
        self.screen.blit(label, (x,y))

    def run(self):
        while not self.gameover:
            self.fall_time += self.clock.get_rawtime()
            self.clock.tick(FPS)

            fall_speed = max(500 - (self.level-1)*50, 100)
            if self.fall_time > fall_speed:
                self.move(0,1)
                self.fall_time = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameover = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move(-1,0)
                    elif event.key == pygame.K_RIGHT:
                        self.move(1,0)
                    elif event.key == pygame.K_DOWN:
                        self.move(0,1)
                    elif event.key == pygame.K_UP:
                        self.rotate_tetromino()

            self.draw_board()

        print(f"Game Over! Score: {self.score}")
        pygame.quit()


if __name__ == "__main__":
    game = GameTetris()
    game.run()
