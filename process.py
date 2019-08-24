import logging
from pathlib import Path
from runpy import run_path
import sys

from wand.image import Image
from schema import SchemaError

from graphics import Graphics

def generate(instance, options):
    try:
        frames = options['duration'] * options['fps']
        delta = 1 / options['fps']
    except KeyError:
        frames = 1
        delta = 0

    for frame in range(frames):
        logging.info('Rendering frame %d...', frame)
        if frame:
            instance.update(delta)

        img = instance.draw()
        if not isinstance(img, Image):
            sys.exit("draw() should return wand.image.Image")

        yield (frame, img)


def process(args):
    options = {}
    class_ = None

    def register(input_class, **kwargs):
        nonlocal class_, options

        if not issubclass(input_class, Graphics):
            sys.exit('Script class should inherit from Graphics')

        class_ = input_class
        options.update(kwargs)

    run_path(args['<script>'], {
        'register': register,
        'Graphics': Graphics,
    })

    props = args['--props']
    
    if 'schema' in options:
        schema = options['schema']

        try:
            props = schema.validate(props)
        except SchemaError as e:
            print("Props don't match schema!", file=sys.stderr)
            sys.exit(e)
    
    for (frame, img) in generate(class_(props), options):
        path = Path(args['-o'] % frame)

        if not path.exists():
            if not path.parent.exists():
                path.parent.mkdir(parents=True)
        else:
            logging.warn('Overwriting %s', path)

        # Autodefine format from string
        img.save(filename=str(path))
        img.close()
