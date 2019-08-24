from schema import Schema, And, Or, Use

from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing

class ColorPropsExample(Graphics):
    def draw(self):
        image = Image(
            width=300, height=300,
            background=Color('black')
        ) 

        with Drawing() as draw:
            draw.fill_color = Color(self.props['color'])
            draw.rectangle(
                left=10, top=10,
                right=290, bottom=290
            )
            draw(image)
        
        return image


register(
    ColorPropsExample,
    schema=Schema({
        'color': Or(str, Use(lambda x: 'rgb({},{},{})'.format(*x)))
    }),
)
