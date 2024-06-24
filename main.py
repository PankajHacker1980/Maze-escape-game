import random

class MazeEscape:
    def __init__(self, size=5):
        self.size = size
        self.grid = [[' '] * size for _ in range(size)]
        self.start = (0, 0)
        self.end = (size - 1, size - 1)
        self.place_walls()
        self.place_start_end()
        self.player_position = self.start
    
    def place_walls(self):
        num_walls = random.randint(self.size, 2 * self.size)
        for _ in range(num_walls):
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if (row, col) != self.start and (row, col) != self.end:
                self.grid[row][col] = '#'
    
    def place_start_end(self):
        self.grid[self.start[0]][self.start[1]] = 'S'
        self.grid[self.end[0]][self.end[1]] = 'E'
    
    def print_maze(self):
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))
    
    def move(self, direction):
        x, y = self.player_position
        if direction == 'up' and x > 0 and self.grid[x - 1][y] != '#':
            self.player_position = (x - 1, y)
        elif direction == 'down' and x < self.size - 1 and self.grid[x + 1][y] != '#':
            self.player_position = (x + 1, y)
        elif direction == 'left' and y > 0 and self.grid[x][y - 1] != '#':
            self.player_position = (x, y - 1)
        elif direction == 'right' and y < self.size - 1 and self.grid[x][y + 1] != '#':
            self.player_position = (x, y + 1)
    
    def play_game(self):
        print("Welcome to Maze Escape!")
        print("Find your way from 'S' (Start) to 'E' (Exit) in the maze.")
        print("Use 'up', 'down', 'left', 'right' to move. '#' represents walls.")
        
        while self.player_position != self.end:
            self.print_maze()
            direction = input("Enter your move (up/down/left/right): ").strip().lower()
            if direction in ['up', 'down', 'left', 'right']:
                self.move(direction)
            else:
                print("Invalid move! Use 'up', 'down', 'left', 'right'.")
        
        self.print_maze()
        print("Congratulations! You reached the exit.")

if __name__ == "__main__":
    game = MazeEscape(size=5)
    game.play_game()
