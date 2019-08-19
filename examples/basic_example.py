colors = [
    (243, 159, 24),
    (205, 91, 69),
    (76, 145, 60),
    (1, 121, 111),
    (175, 64, 53)
]

def draw(drawing, state):
    for i in range(5):
        offset = (i + 1) * 20
        topleft = (offset, offset) 
        bottomright = (200 + offset, 200 + offset)
        drawing.rectangle(
            [topleft, bottomright],
            fill=colors[i]
        )

register(
    (300, 300),
    mode='RGB'
)
