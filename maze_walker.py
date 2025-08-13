
from ursina import *

class MazeWalker:
    def __init__(self, maze, start=(1, 1), end=None):
        self.maze = maze
        self.maze_width = len(maze[0])
        self.maze_height = len(maze)
        self.start = start
        self.end = end or (self.maze_width - 2, self.maze_height - 2)

        self.path = self.find_path(self.start, self.end)
        self.walk_path(self.path)

    def find_path(self, start, end):
        from collections import deque
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            (x, z), path = queue.popleft()
            if (x, z) == end:
                return path
            for dx, dz in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, nz = x+dx, z+dz
                if 0 <= nx < self.maze_width and 0 <= nz < self.maze_height:
                    if self.maze[nz][nx] == 0 and (nx, nz) not in visited:
                        visited.add((nx, nz))
                        queue.append(((nx, nz), path + [(nx, nz)]))
        return []

    def walk_path(self, path, step=0):
        if not path:
            print("No path found.")
            return

        if step >= len(path):
            step = 0  # Loop back to start

        x, z = path[step]
        next_pos = Vec3(x, 0.7, z)
        camera.animate_position(next_pos, duration=0.5)

        # Optional: rotate camera based on direction
        if step + 1 < len(path):
            dx = path[step+1][0] - x
            dz = path[step+1][1] - z
            if dx == 1: rot = Vec3(0, 90, 0)
            elif dx == -1: rot = Vec3(0, -90, 0)
            elif dz == 1: rot = Vec3(0, 0, 0)
            elif dz == -1: rot = Vec3(0, 180, 0)
            camera.animate_rotation(rot, duration=0.5)

        invoke(lambda: self.walk_path(path, step+1), delay=0.5)
