# animate.py

Utility to create motion graphics with Python scripts.
It uses [Wand][wand-py.org] to generate images.

## Usage

```shell
main.py [options] <script> [-o <output>]
```

- `script` is a Python script to use.
- `-o <output>` specifies output directory. It has to be a printf-style
string with single number input for frame. By default it renders to
`./render/%03d.png` relative to working directory.

### Options

- `--props=<value>` JSON encoded properties for graphics. If script
declares a schema input will be validated against it.

## Scripts

Scripts must define a `draw()` function which returns a `wand.image.Image`.
Also there are optional `init()` to initialize state
and `update()` to update it.

Here's the example:

```python
from schema import Schema
from wand.color import Color
from wand.image import Image

def init(props):
    """
    Initializes a state

    Arguments:
    - props - data passed by '--props' option or None.
    """

    return {
        'color': props['color']
    }

def update(delta, state):
    """
    Updates a state

    It isn't called at first frame.

    Arguments:
    - delta - time in seconds from last frame. It's always 1 / FPS.
    - state - previous frame's state.

    Returns new state
    """

    return state

def draw(state):
    """
    Generates the image

    It's called after update() changes the state.

    Arguments:
    - state - current frame's state.

    Returns wand.image.Image
    """

    return Image(
        width=256, height=256,
        background=Color(state['color'])
    )

"""
Optional register hook

If you don't pass any of duration or fps, animation
will long 1 frame.

Parameters:
- duration - how does the animation long in seconds.
- fps - animation's framerate.
- schema - Python Schema to validate provided data against.
"""
register(
    duration=20,
    fps=25,
    schema=Schema({
        'color': str
    })
)
```

Other examples may be found in [examples folder](examples)
