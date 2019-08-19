"""Usage:
    main.py [options] <script> [-o <output>]
    main.py (-h | --help)
    main.py --version

Options:
    -h --help     Show this screen.
    -o FILE       Output file pattern [default: ./render/%03d.png]
    -v --verbose  Display additional information

"""
import logging
from os import path
import sys

from docopt import docopt
from schema import Schema, SchemaError, And, Or

from process import process

__ver__ = "0.1.1"

if __name__ == "__main__":
    arguments = docopt(__doc__, version=__ver__)

    schema = Schema({
        '<script>': And(path.isfile, error='Script should exist!'),
        '-o': str,
        '--verbose': bool,
        '--help': False,
    })

    try:
        arguments = schema.validate(arguments)
    except SchemaError as e:
        sys.exit(e)
    
    if arguments['--verbose']:
        logging.basicConfig(level=logging.DEBUG)

    process(arguments)
