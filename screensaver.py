from ursina import *
from pathlib import Path
from maze_generator import generate_maze
from renderer import draw_wall
from maze_walker import MazeWalker

application.asset_folder = Path(__file__).parent
app = Ursina()

# Generate or hardcode maze
maze = generate_maze(21, 21)

# Render walls
for z, row in enumerate(maze):
    for x, cell in enumerate(row):
        if cell == 1:
            draw_wall(x, z, collider='box')

# Render floor
maze_width = len(maze[0])
maze_height = len(maze)
Entity(
    model='plane',
    scale=(maze_width, 1, maze_height),
    texture='textures/floor.png',
    position=(maze_width // 2, 0, maze_height // 2),  # Y = 0
    collider='box',
    color=color.white
)

# Lighting
DirectionalLight().look_at(Vec3(1, -1, -1))
AmbientLight(color=color.rgb(100, 100, 100))

# Wider field of view to prevent camera clipping
camera.fov = 90

#Keeps camera within corridors of maze
walker = MazeWalker(maze)

app.run()
