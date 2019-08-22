from schema import Schema, And, Use

def draw(im, state):
    im.rectangle(
        [10, 10, 290, 290],
        fill=state['color']
    )


def init(props):
    return {
        'color': tuple(props['color'])
    }

register(
    (300, 300),
    mode='RGB',
    schema=Schema({
        'color': And(Use(tuple), lambda x: len(x) >= 3)
    }),
)
