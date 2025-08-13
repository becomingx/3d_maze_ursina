import random

def generate_maze(width, height):
    """Generate a simple maze using recursive backtracking."""
    maze = [[1 for _ in range(width)] for _ in range(height)]

    def carve(x, y):
        dirs = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width - 1 and 1 <= ny < height - 1 and maze[ny][nx] == 1:
                maze[ny - dy // 2][nx - dx // 2] = 0
                maze[ny][nx] = 0
                carve(nx, ny)

    maze[1][1] = 0
    carve(1, 1)
    return maze

