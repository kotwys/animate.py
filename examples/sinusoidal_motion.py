import math

SCREEN_HEIGHT = 300
SHAPE_SIDE = 100
AMPLITUDE = (SCREEN_HEIGHT - SHAPE_SIDE) / 2

def update(delta, state):
    return state + delta

def draw(drawing, state):
    position = round((math.sin(state) + 1) * AMPLITUDE)

    drawing.rectangle(
        [0, position, 100, position + 100],
        fill=(255, 255, 255)
    )

def init():
    return 0

register(
    (100, 300),
    mode='L',
    fps=25,
    duration=5
)
