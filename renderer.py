from ursina import Entity, color

def draw_wall(x, z, texture='textures/wall.png', collider='box'):
    Entity(
        model='cube',
        position=(x, 1, z),
        scale=(1, 2, 1),
        texture=texture,
        color=color.white,
        collider=collider
    )
