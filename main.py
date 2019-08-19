from os import path
from sys import argv
from process import process

def main():
    options = argv[1:]

    if not options:
        print('No script specified')
        return

    if path.isfile(options[0]):
        script = options[0]
    else:
        print("Script file doesn't exist!")
        return

    if len(options) > 1:
        output = options[1]
    else:
        output = './render/frame_%04d.png'

    process(script, output)

if __name__ == "__main__":
    main()
