import math

from wand.color import Color
from wand.image import Image

SCREEN_HEIGHT = 300
SHAPE_SIDE = 100
AMPLITUDE = (SCREEN_HEIGHT - SHAPE_SIDE) / 2

def update(delta, state):
    return state + delta

def draw(state):
    image = Image(
        width=100, height=300,
        background=Color('black')
    )

    with Image(width=100, height=100, pseudo='xc:white') as rect:
        position = round((math.sin(state) + 1) * AMPLITUDE)
        image.composite(rect, top=position)
    
    return image

def init(props):
    return 0

register(
    fps=25,
    duration=5
)
