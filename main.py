class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.path = []
        self.visited = set()

    def get_start_end(self):
        start = None
        end = None
        for r in range(self.rows):
            for c in range(self.cols):
                if self.maze[r][c] == 'S':
                    start = (r, c)
                elif self.maze[r][c] == 'E':
                    end = (r, c)
        return start, end

def is_valid(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            if self.maze[row][col] != 1 and (row, col) not in self.visited:
                return True
        return False

    def get_neighbors(self, row, col):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dr, dc in directions:
            neighbors.append((row + dr, col + dc))
        return neighbors
