from runpy import run_path
from PIL import Image, ImageDraw

def process(script, output):
    # default values
    size = None
    mode = 'RGBA'

    def register(movie_size, **kwargs):
        nonlocal size, mode

        size = movie_size
        if kwargs['mode']:
            mode = kwargs['mode']

    module = run_path(script, {
        'register': register,
    })

    if 'draw' not in module:
        print('No draw() function in script!')
        return

    img = Image.new(mode, size)

    draw = ImageDraw.Draw(img)
    module['draw'](draw)

    img.show()
