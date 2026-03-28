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
