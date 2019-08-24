import math

from wand.color import Color
from wand.image import Image

SCREEN_HEIGHT = 300
SHAPE_SIDE = 100
AMPLITUDE = (SCREEN_HEIGHT - SHAPE_SIDE) / 2

class SinusoidalMotion:
    def __init__(self, props):
        self.state = 0
    
    def update(self, delta):
        self.state += delta
    
    def draw(self):
        image = Image(
            width=100, height=300,
            background=Color('black')
        )

        with Image(width=100, height=100, pseudo='xc:white') as rect:
            position = round((math.sin(self.state) + 1) * AMPLITUDE)
            image.composite(rect, top=position)
        
        return image


register(
    SinusoidalMotion,
    fps=25,
    duration=5
)
