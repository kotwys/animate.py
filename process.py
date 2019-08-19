from pathlib import Path
from runpy import run_path
from PIL import Image, ImageDraw

def process(script, output):
    # default values
    options = {
        'mode': 'RGBA'
    }

    def register(movie_size, **kwargs):
        nonlocal options

        options['size'] = movie_size
        options.update(kwargs)

    module = run_path(script, {
        'register': register,
    })

    if 'draw' not in module:
        print('No draw() function in script!')
        return

    img = Image.new(options['mode'], options['size'])

    draw = ImageDraw.Draw(img)
    module['draw'](draw)

    path = Path(output % 0)

    if not path.exists():
        if not path.parent.exists():
            path.parent.mkdir(parents=True)
    else:
        print('Overwritting {}'.format(path))

    img.save(path)
