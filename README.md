A proof of concept throwback to the old 3d maze screensaver from Windows 95 built with Python and Ursina for Linux.

## Author: Patricia Tirado 
Follow me on LinkedIn: 
www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=patriciatirado29a 
'Forging better outcomes with uncommon sense".

## Texture credits:
https://opengameart.org/content/zortch-2-rejected-textures-crackwalltilepng
https://opengameart.org/content/zortch-2-rejected-textures-crackwalltilepng

# Maze Screensaver Game
A modular, visually engaging maze exploration experience built with [Ursina Engine](https://www.ursinaengine.org/). 
This hybrid screensaver/game renders procedurally generated mazes and lets you navigate them with smooth camera transitions and ambient lighting.

## File Structure
maze-screensaver/
├── main.py               # Entry point
├── maze_generator.py     # Maze generation logic
├── renderer.py           # Wall rendering utilities
├── maze_walker.py        # Camera movement and collision logic
├── textures/
    └── floor.png         # Floor texture
    └── wall.png          # Wall Texture

## Customization Notes
Change maze size in main.py:
- maze = generate_maze(width, height)
- Swap textures by replacing textures/floor.png
- Modify camera behavior in maze_walker.py for cinematic or gameplay modes

## Features
- Procedural maze generation using customizable dimensions
- Modular wall rendering and textured floor
- Cinematic lighting with directional and ambient sources
- First-person camera logic that stays within maze corridors
- Wide field of view for immersive navigation
- Easily extendable architecture for gameplay or screensaver modes

## Installation
- Clone the repository
  Bash:
      git clone https://github.com/yourusername/maze-screensaver.git, or download the file as a .zip directly from Github.com
   
- Make sure you have Python 3.8+ and install Ursina:
      pip install ursina

- Run the script:
      python screensaver.py
