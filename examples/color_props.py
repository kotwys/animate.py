from schema import Schema, And, Or, Use

from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing

def draw(state):
    image = Image(
        width=300, height=300,
        background=Color('black')
    ) 

    with Drawing() as draw:
        draw.fill_color = Color(state['color'])
        draw.rectangle(
            left=10, top=10,
            right=290, bottom=290
        )
        draw(image)
    
    return image


def init(props):
    return props

register(
    schema=Schema({
        'color': Or(str, Use(lambda x: 'rgb({},{},{})'.format(*x)))
    }),
)
