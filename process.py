import logging
from pathlib import Path
from runpy import run_path
import sys

from PIL import Image, ImageDraw

def generate(module, options):
    try:
        frames = options['duration'] * options['fps']
        delta = 1 / options['fps']
    except KeyError:
        frames = 1
        delta = 0

    if 'init' in module:
        state = module['init']()
    else:
        state = None

    has_update = 'update' in module

    for frame in range(frames):
        logging.info('Rendering frame %d...', frame)
        im = Image.new(options['mode'], options['size'])
        draw = ImageDraw.Draw(im)

        if frame and has_update:
            state = module['update'](delta, state)
        
        module['draw'](draw, state)
        yield (frame, im) 


def process(args):
    # default values
    options = {
        'mode': 'RGBA'
    }

    def register(movie_size, **kwargs):
        nonlocal options

        options['size'] = movie_size
        options.update(kwargs)

    module = run_path(args['<script>'], {
        'register': register,
    })

    if 'draw' not in module:
        sys.exit('No draw() function in script!')

    for (frame, img) in generate(module, options):
        path = Path(args['-o'] % frame)

        if not path.exists():
            if not path.parent.exists():
                path.parent.mkdir(parents=True)
        else:
            logging.warn('Overwriting %s', path)

        img.save(path)
