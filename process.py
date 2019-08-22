import logging
from pathlib import Path
from runpy import run_path
import sys

from wand.image import Image
from schema import SchemaError

def generate(module, options):
    try:
        frames = options['duration'] * options['fps']
        delta = 1 / options['fps']
    except KeyError:
        frames = 1
        delta = 0

    if 'init' in module:
        state = module['init'](options['props'])
    else:
        state = None

    has_update = 'update' in module

    for frame in range(frames):
        logging.info('Rendering frame %d...', frame)
        if frame and has_update:
            state = module['update'](delta, state)

        img = module['draw'](state)
        yield (frame, img)


def process(args):
    options = {}

    def register(**kwargs):
        nonlocal options
        options.update(kwargs)

    module = run_path(args['<script>'], {
        'register': register,
    })

    props = args['--props']
    
    if 'schema' in options:
        schema = options['schema']

        try:
            props = schema.validate(props)
        except SchemaError as e:
            print("Props don't match schema!", file=sys.stderr)
            sys.exit(e)
    
    options['props'] = props

    if 'draw' not in module:
        sys.exit('No draw() function in script!')

    for (frame, img) in generate(module, options):
        path = Path(args['-o'] % frame)

        if not path.exists():
            if not path.parent.exists():
                path.parent.mkdir(parents=True)
        else:
            logging.warn('Overwriting %s', path)

        # Autodefine format from string
        img.save(filename=str(path))
        img.close()
