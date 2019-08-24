from wand.color import Color
from wand.image import Image
from wand.drawing import Drawing

colors = [
    '#f39f18',
    '#cd5b45',
    '#4c913c',
    '#01796f',
    '#af4035'
]

class BasicExample(Graphics):
    def draw(self):
        image = Image(
            width=300, height=300,
            background=Color('black')
        )

        with Drawing() as draw:
            for i in range(5):
                offset = (i + 1) * 20
                draw.fill_color = Color(colors[i])
                draw.rectangle(
                    left=offset, top=offset,
                    right=200+offset, bottom=200+offset
                )
            draw(image)
        
        return image


register(BasicExample)
