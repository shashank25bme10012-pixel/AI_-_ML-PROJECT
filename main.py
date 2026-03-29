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
def solve(self):
        start, end = self.get_start_end()
        if not start or not end:
            return None

        stack = [(start, [start])]
        
        while stack:
            (curr_row, curr_col), current_path = stack.pop()
            
            if (curr_row, curr_col) == end:
                self.path = current_path
                return self.path
            
            if (curr_row, curr_col) not in self.visited:
                self.visited.add((curr_row, curr_col))
                
                for next_row, next_col in self.get_neighbors(curr_row, curr_col):
                    if self.is_valid(next_row, next_col):
                        new_path = list(current_path)
                        new_path.append((next_row, next_col))
                        stack.append(((next_row, next_col), new_path))
        return None
