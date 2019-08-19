"""Usage:
    main.py [-f] <script> [-o <output>]
    main.py (-h | --help)

Options:
    -h --help  Show this screen.
    -o FILE    Output file pattern [default: ./render/%03d.png]

"""
from os import path

from docopt import docopt
from schema import Schema, SchemaError, And, Or

from process import process

if __name__ == "__main__":
    arguments = docopt(__doc__)

    schema = Schema({
        '<script>': And(path.isfile, error='Script should exist!'),
        '-o': str,
        '--help': False,
    })

    try:
        arguments = schema.validate(arguments)
    except SchemaError as e:
        exit(e)

    process(arguments)
