from sys import argv
from process import process

def main():
    options = argv[1:]

    if not options:
        print('No script specified')
        return

    script = options[0]

    if len(options) > 1:
        output = options[1]
    else:
        output = 'auto'

    process()

if __name__ == "__main__":
    main()
